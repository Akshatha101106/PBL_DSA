
import sys
from pathlib import Path
import subprocess
import json
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

from Python_Code import student_data , database

def run_cpp():
    result = subprocess.run(
        ["source_code/main_file.exe"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def load_json():
    try:
        with open("result.json", "r") as j:
            return json.load(j)
    except FileNotFoundError:
        return None

def get_score_color(score):
    """Return color based on score threshold"""
    if score >= 8:
        return "#28a745"  # Green
    elif score >= 5:
        return "#ffc107"  # Yellow
    else:
        return "#dc3545"  # Red

def get_eligibility_status(score):
    """Return eligibility message based on score"""
    if score >= 8:
        return "✅ Highly Eligible"
    elif score >= 5:
        return "⚠️ Moderately Eligible"
    else:
        return "❌ Not Currently Eligible"


def create_skills_chart(matched_skills, skill_gap):
    """Create a donut chart for skills match"""
    fig, ax = plt.subplots(figsize=(6, 6))
    
    matched_count = len(matched_skills)
    gap_count = len(skill_gap)
    
    sizes = [matched_count, gap_count]
    labels = ['Matched Skills', 'Skill Gaps']
    colors = ['#5B8FF9', '#FF6B6B']
    explode = (0.05, 0.05)
    
    wedges, texts, autotexts = ax.pie(
        sizes, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        explode=explode,
        textprops={'fontsize': 12, 'weight': 'bold'}
    )
    
    # Draw circle in center for donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.axis('equal')
    plt.title('Skills Analysis', fontsize=14, weight='bold', pad=20)
    
    return fig

def create_score_gauge(score, max_score=10):
    """Create a gauge chart for the score"""
    fig, ax = plt.subplots(figsize=(8, 4), subplot_kw={'projection': 'polar'})
    
    # Normalize score to angle (0 to 180 degrees)
    theta = np.linspace(0, np.pi, 100)
    
    # Background arc
    ax.plot(theta, [1]*100, color='#e0e0e0', linewidth=20)
    
    # Score arc
    score_theta = np.linspace(0, np.pi * (score / max_score), 100)
    color = get_score_color(score)
    ax.plot(score_theta, [1]*100, color=color, linewidth=20)
    
    # Add score text in center
    ax.text(0, 0, f'{score:.1f}/{max_score}', 
            ha='center', va='center', fontsize=24, weight='bold')
    
    ax.set_ylim(0, 1.5)
    ax.set_theta_offset(np.pi)
    ax.set_theta_direction(-1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)
    ax.grid(False)
    
    plt.title('Overall Score', fontsize=14, weight='bold', pad=30)
    
    return fig

# Streamlit Configuration
st.set_page_config(
    page_title="Student Resume Analyzer", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #1e3c72 50%, #2a5298 100%);
    }
    .main-header {
        font-size: 2.2rem;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #e0e7ff;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .company-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #5B8FF9;
        margin-bottom: 1rem;
    }
    .skill-tag {
        display: inline-block;
        background-color: #5B8FF9;
        color: white;
        padding: 0.4rem 0.9rem;
        border-radius: 18px;
        margin: 0.3rem;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .gap-tag {
        display: inline-block;
        background-color: #FF6B6B;
        color: white;
        padding: 0.4rem 0.9rem;
        border-radius: 18px;
        margin: 0.3rem;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .skills-section {
        background-color: rgba(240, 248, 255, 0.95);
        padding: 1.2rem;
        border-radius: 12px;
        margin: 0.8rem 0;
    }
    .skills-header {
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 0.8rem;
        color: #2c3e50;
    }
    .ai-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.8rem 0;
        font-size: 0.95rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .resource-link {
        display: block;
        margin: 0.5rem 0;
        padding: 0.6rem;
        background-color: white;
        border-radius: 5px;
        border-left: 3px solid #5B8FF9;
        transition: all 0.3s ease;
    }
    .resource-link:hover {
        background-color: #f0f9ff;
        transform: translateX(5px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .resource-link a {
        color: #5B8FF9;
        text-decoration: none;
        font-weight: 500;
    }
    .resource-link a:hover {
        color: #1e3c72;
    }
    /* Card styling */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">🎓 Student Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload your resume and discover your perfect company match</div>', unsafe_allow_html=True)

# File Upload Section
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        uploaded_file = st.file_uploader(
            label="Upload Resume (PDF)",
            type=["pdf"],
            help="Upload your resume in PDF format only"
        )
        
        button_clicked = st.button("🔍 Analyze Resume", use_container_width=True, type="primary")

# Process Resume
if button_clicked:
    if uploaded_file is None:
        st.warning("⚠️ Please upload a PDF file to proceed.")
    elif not uploaded_file.name.lower().endswith(".pdf"):
        st.error("❌ Invalid file format! Please upload a PDF file.")
    else:
        with st.spinner("Analyzing your resume..."):
            name = student_data.process_all_resume_data(uploaded_file)
            run_cpp()
            data = load_json()
        
        if data and name:
            st.success("✅ Resume analyzed successfully!")
            st.snow()
            
            # Welcome Message with styling
            st.markdown(f"""
                <div style='background-color: rgba(255, 255, 255, 0.9); padding: 1.5rem; 
                     border-radius: 15px; margin-bottom: 1rem; text-align: center;'>
                    <h2 style='color: #1e3c72; margin: 0;'>Hello, {name}! 👋</h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Display Candidate Branch if available
            if "candidate_branch" in data:
                st.markdown(f"""
                    <div style='background-color: rgba(255, 255, 255, 0.9); padding: 0.8rem; 
                         border-radius: 10px; margin-bottom: 1rem; text-align: center;'>
                        <strong style='color: #1e3c72;'>Branch:</strong> 
                        <span style='color: #5B8FF9; font-size: 1.1rem;'>{data['candidate_branch']}</span>
                    </div>
                """, unsafe_allow_html=True)
            
            # Matched Companies Section
            if "matched_companies" in data and data["matched_companies"]:
                st.markdown("""
                    <div style='background-color: rgba(255, 255, 255, 0.9); padding: 1rem; 
                         border-radius: 10px; margin-bottom: 1rem;'>
                        <h2 style='color: #1e3c72; margin: 0;'>🏢 Matched Companies</h2>
                    </div>
                """, unsafe_allow_html=True)
                
                for idx, company in enumerate(data["matched_companies"]):
                    company_name = company.get("company", "Unknown Company")
                    role = company.get("role", "N/A")
                    score = company.get("score", 0)
                    matched_skills = company.get("matched_skills", [])
                    skill_gap = company.get("skill_gap", [])
                    
                    # Company Card
                    with st.expander(f"**{company_name}** - {role}", expanded=(idx == 0)):
                        # Score Display and Role in single row
                        score_color = get_score_color(score)
                        eligibility = get_eligibility_status(score)
                        
                        st.markdown(f"""
                            <div style='background-color: {score_color}; color: white; padding: 1rem; 
                                 border-radius: 10px; text-align: center; margin-bottom: 1rem;'>
                                <h3 style='margin: 0;'>Score: {score}/10</h3>
                                <p style='margin: 0.3rem 0 0 0; font-size: 1rem;'>{eligibility}</p>
                                <p style='margin: 0.3rem 0 0 0; font-size: 0.9rem;'>Role: {role}</p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Create two columns for skills to fill space
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            # Matched Skills
                            st.markdown("""
                                <div class='skills-section'>
                                    <div class='skills-header'>✅ Matched Skills</div>
                            """, unsafe_allow_html=True)
                            
                            if matched_skills:
                                skills_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in matched_skills])
                                st.markdown(skills_html, unsafe_allow_html=True)
                            else:
                                st.write("No matched skills found.")
                            
                            st.markdown("</div>", unsafe_allow_html=True)
                        
                        with col2:
                            # Skill Gaps
                            if skill_gap:
                                st.markdown("""
                                    <div class='skills-section' style='background-color: rgba(255, 245, 245, 0.95);'>
                                        <div class='skills-header'>📚 Skills to Develop</div>
                                """, unsafe_allow_html=True)
                                
                                gap_html = "".join([f'<span class="gap-tag">{skill}</span>' for skill in skill_gap])
                                st.markdown(gap_html, unsafe_allow_html=True)
                                
                                st.markdown("</div>", unsafe_allow_html=True)
                            else:
                                st.markdown("""
                                    <div class='skills-section' style='background-color: rgba(220, 252, 231, 0.95);'>
                                        <div class='skills-header'>🎉 All Skills Matched!</div>
                                        <p style='margin: 0; color: #059669;'>Great! You have all the required skills!</p>
                                    </div>
                                """, unsafe_allow_html=True)
                        
                        # Learning Resources Section (Full Width)
                        if skill_gap:
                            st.markdown("""
                                <div class='skills-section' style='background-color: rgba(240, 249, 255, 0.95); margin-top: 1rem;'>
                                    <div class='skills-header'>🎓 Recommended Learning Resources</div>
                                    <p style='color: #666; font-size: 0.9rem; margin-bottom: 1rem;'>
                                        Here are some free courses to help you develop the required skills:
                                    </p>
                            """, unsafe_allow_html=True)
                            
                            resources_found = False
                            for skill in skill_gap:
                                resources = database.get_skill_resources(skill)
                                if resources:
                                    resources_found = True
                                    st.markdown(f"<strong style='color: #1e3c72; font-size: 1.05rem;'>📌 {skill}:</strong>", unsafe_allow_html=True)
                                    for resource in resources:
                                        st.markdown(f"""
                                            <div style='margin: 0.5rem 0; padding: 0.7rem; background-color: white; 
                                                 border-radius: 8px; border-left: 4px solid #5B8FF9;
                                                 transition: all 0.3s ease;'>
                                                <a href='{resource["url"]}' target='_blank' 
                                                   style='color: #5B8FF9; text-decoration: none; font-weight: 500;
                                                          display: flex; align-items: center;'>
                                                    <span style='margin-right: 8px;'>▶️</span>
                                                    <span>{resource["title"]}</span>
                                                </a>
                                            </div>
                                        """, unsafe_allow_html=True)
                                    st.markdown("<div style='margin-bottom: 0.8rem;'></div>", unsafe_allow_html=True)
                            
                            if not resources_found:
                                st.markdown("""
                                    <p style='color: #666; font-style: italic; margin: 0.5rem 0;'>
                                        💡 No specific course recommendations available for these skills. 
                                        Try searching on YouTube, Coursera, or Udemy!
                                    </p>
                                """, unsafe_allow_html=True)
                            
                            st.markdown("</div>", unsafe_allow_html=True)
                        
                        # AI Message below resources
                        if skill_gap:
                            skill_gap_text = ", ".join(skill_gap)
                            st.markdown(f"""
                                <div class='ai-message'>
                                    🤖 <strong>AI Insight:</strong> To be fully eligible for this role at {company_name}, 
                                    focus on developing: <strong>{skill_gap_text}</strong>. 
                                    Consider the courses above or build projects to bridge these gaps!
                                </div>
                            """, unsafe_allow_html=True)
                        
                        # Skills Analysis Chart - Compact version
                        if matched_skills or skill_gap:
                            col_chart1, col_chart2 = st.columns([1, 1])
                            
                            with col_chart1:
                                st.markdown("**📊 Skills Breakdown**")
                                skills_fig = create_skills_chart(matched_skills, skill_gap)
                                st.pyplot(skills_fig)
                                plt.close()
                            
                            with col_chart2:
                                st.markdown("**📈 Score Gauge**")
                                if score > 0:
                                    gauge_fig = create_score_gauge(score)
                                    st.pyplot(gauge_fig)
                                    plt.close()
                        
                        st.markdown("<hr style='margin: 1rem 0;'>", unsafe_allow_html=True)
            
            else:
                st.warning("⚠️ No company matches found. Consider expanding your skill set!")
                
        else:
            st.error("❌ Could not extract data from the resume. Please try again with a different file.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: white; padding: 1rem;'>
        <p style='margin: 0;'>💡 <strong>Tip:</strong> Keep your resume updated with your latest skills and projects for better matches!</p>
        <p style='margin: 0.5rem 0 0 0; font-size: 0.85rem; opacity: 0.8;'>
            All course recommendations are from FreeCodeCamp and other free resources on YouTube
        </p>
    </div>
""", unsafe_allow_html=True)