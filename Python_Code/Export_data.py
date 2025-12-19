import pdfplumber
import re
from typing import Dict, List
from .database import (
    create_comprehensive_skill_database,
    format_skill_name
)

def extract_data_from_pdf(pdf_path):
    """
    Extracts and returns all text from a PDF file.
    """
    line_data  = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            data_in_page = page.extract_text()
            if data_in_page:
                line_data += data_in_page +'\n'
    return line_data

def clean_the_data(resume_data):
    """
    When data is being received, it may contain extra spaces or noise.
    This function cleans the data before further processing.
    """
    line = []

    for t in resume_data.splitlines():
        t  = t.strip()
        if t:
            line.append(t)
    return line

def extract_name_from_data(cleaned_Data) -> str:
    """
    A simple function to extract the name from cleaned resume data.
    """
    list_name = []
    if cleaned_Data:
        first_line = cleaned_Data[0]
        if len(first_line) >= 1:
            name_Split = first_line.split() 
            for name in name_Split:
                    list_name.append(name)
        return " ".join(list_name)
    return "Name not found"

def extract_skills_from_data(cleaned_Data: List[str]) -> Dict[str, List[str]]:
    """
    Universal skills extractor that works with ANY resume format.
    Uses multiple intelligent strategies to find skills regardless of structure.
    """
    
    # Comprehensive skill database with variations
    skill_database = create_comprehensive_skill_database()
    
    # Strategy 1: Find and extract from SKILLS section (if exists)
    skills_from_section = extract_from_skills_section_flexible(cleaned_Data, skill_database)
    
    # Strategy 2: Scan entire resume for skill mentions
    skills_from_global = extract_skills_from_entire_resume(cleaned_Data, skill_database)
    
    # Strategy 3: Extract from bullet points and lists
    skills_from_bullets = extract_from_bullet_points(cleaned_Data, skill_database)
    
    # Strategy 4: Pattern-based extraction (lines with multiple tech terms)
    skills_from_patterns = extract_using_tech_density(cleaned_Data, skill_database)
    
    # Merge all strategies
    all_skills = merge_and_deduplicate(
        skills_from_section,
        skills_from_global,
        skills_from_bullets,
        skills_from_patterns
    )
    
    # Categorize the skills intelligently
    categorized_skills = smart_categorize_skills(all_skills, skill_database)
    
    # Clean up and format
    final_skills = cleanup_and_format(categorized_skills)
    
    return final_skills


def extract_from_skills_section_flexible(cleaned_Data: List[str], skill_db: Dict) -> List[str]:
    """
    Extract skills from SKILLS section with flexible parsing.
    """
    skills = []
    in_skills = False
    section_end_keywords = ['experience', 'projects', 'education', 'certifications', 'achievements']
    
    for i, line in enumerate(cleaned_Data):
        line_lower = line.lower().strip()
        
        # Detect SKILLS section start
        if line_lower == 'skills' or line_lower == 'technical skills':
            in_skills = True
            continue
        
        # Detect section end
        if in_skills and line_lower in section_end_keywords:
            break
        
        # Extract skills from lines in SKILLS section
        if in_skills:
            detected = detect_skills_in_text(line, skill_db)
            skills.extend(detected)
    
    return skills


def extract_skills_from_entire_resume(cleaned_Data: List[str], skill_db: Dict) -> List[str]:
    """
    Scan entire resume for skill mentions.
    """
    skills = []
    
    for line in cleaned_Data:
        detected = detect_skills_in_text(line, skill_db)
        skills.extend(detected)
    
    return skills


def extract_from_bullet_points(cleaned_Data: List[str], skill_db: Dict) -> List[str]:
    """
    Extract skills specifically from bullet point lines.
    """
    skills = []
    bullet_patterns = [r'^[•\-\*]', r'^[\d]+\.']
    
    for line in cleaned_Data:
        # Check if line starts with bullet
        if any(re.match(pattern, line.strip()) for pattern in bullet_patterns):
            detected = detect_skills_in_text(line, skill_db)
            skills.extend(detected)
    
    return skills


def extract_using_tech_density(cleaned_Data: List[str], skill_db: Dict) -> List[str]:
    """
    Find lines with high density of technical terms (likely skill lists).
    """
    skills = []
    
    for line in cleaned_Data:
        detected = detect_skills_in_text(line, skill_db)
        
        # If line has 2+ skills, it's likely a skill list
        if len(detected) >= 2:
            skills.extend(detected)
    
    return skills


def detect_skills_in_text(text: str, skill_db: Dict) -> List[str]:
    """
    Detect all skills mentioned in a piece of text using fuzzy matching.
    """
    detected = []
    text_lower = text.lower()
    
    # Remove common prefixes that might confuse detection
    text_lower = re.sub(r'basic knowledge of |knowledge of |experience in |worked with |idea on |basics of |knowledge on |idea of |worked on |fair idea on |basic idea of', '', text_lower)
    
    for skill_name, skill_info in skill_db.items():
        # Check all variations of the skill
        for variation in skill_info['variations']:
            # Use word boundaries for better matching
            pattern = r'\b' + re.escape(variation) + r'\b'
            
            if re.search(pattern, text_lower):
                # Extract the actual text from original (preserve casing)
                match = re.search(pattern, text_lower)
                if match:
                    start, end = match.span()
                    # Get original case
                    original_text = text[start:end]
                    detected.append(skill_name)
                    break  # Found one variation, don't need to check others
    
    return detected


def merge_and_deduplicate(skills1: List[str], skills2: List[str], 
                        skills3: List[str], skills4: List[str]) -> List[str]:
    """
    Merge multiple skill lists and remove duplicates.
    """
    all_skills = skills1 + skills2 + skills3 + skills4
    
    # Remove duplicates while preserving order
    seen = set()
    unique_skills = []
    
    for skill in all_skills:
        skill_lower = skill.lower()
        if skill_lower not in seen:
            seen.add(skill_lower)
            unique_skills.append(skill)
    
    return unique_skills


def smart_categorize_skills(skills: List[str], skill_db: Dict) -> Dict[str, List[str]]:
    """
    Categorize skills intelligently based on the skill database.
    """
    categorized = {}
    
    for skill in skills:
        skill_lower = skill.lower()
        
        if skill_lower in skill_db:
            category = skill_db[skill_lower]['category']
            
            if category not in categorized:
                categorized[category] = []
            
            # Use proper formatting
            categorized[category].append(format_skill_name(skill_lower, skill_db))
    
    return categorized

def cleanup_and_format(categorized: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Final cleanup: remove empty categories, sort skills.
    """
    cleaned = {}
    
    for category, skills in categorized.items():
        if skills:
            # Remove duplicates (case-insensitive)
            unique = []
            seen = set()
            for skill in skills:
                if skill.lower() not in seen:
                    seen.add(skill.lower())
                    unique.append(skill)
            
            # Sort alphabetically
            unique.sort()
            cleaned[category] = unique
    
    return cleaned
