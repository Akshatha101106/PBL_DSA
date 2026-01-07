from typing import Dict
import re

def create_comprehensive_skill_database() -> Dict[str, Dict]:
    """
    Create a comprehensive database of skills with metadata for intelligent categorization.
    """
    return {
        # Programming Languages
        'python': {'category': 'Programming Languages', 'variations': ['python', 'py'], 'type': 'language'},
        'java': {'category': 'Programming Languages', 'variations': ['java'], 'type': 'language'},
        'javascript': {'category': 'Programming Languages', 'variations': ['javascript', 'js'], 'type': 'language'},
        'c': {'category': 'Programming Languages', 'variations': ['c'], 'type': 'language'},
        'c++': {'category': 'Programming Languages', 'variations': ['c++', 'cpp', 'cplusplus'], 'type': 'language'},
        'c#': {'category': 'Programming Languages', 'variations': ['c#', 'csharp'], 'type': 'language'},
        'php': {'category': 'Programming Languages', 'variations': ['php'], 'type': 'language'},
        'ruby': {'category': 'Programming Languages', 'variations': ['ruby'], 'type': 'language'},
        'swift': {'category': 'Programming Languages', 'variations': ['swift'], 'type': 'language'},
        'kotlin': {'category': 'Programming Languages', 'variations': ['kotlin'], 'type': 'language'},
        'go': {'category': 'Programming Languages', 'variations': ['golang', 'go'], 'type': 'language'},
        'rust': {'category': 'Programming Languages', 'variations': ['rust'], 'type': 'language'},
        'typescript': {'category': 'Programming Languages', 'variations': ['typescript', 'ts'], 'type': 'language'},
        'sql': {'category': 'Programming Languages', 'variations': ['sql'], 'type': 'language'},
        'r': {'category': 'Programming Languages', 'variations': ['r programming'], 'type': 'language'},
        'shell scripting': {'category': 'Programming Languages', 'variations': ['shell scripting', 'bash','shell script','shell'], 'type': 'language'},
        'cmake': {'category': 'Programming Languages', 'variations': ['cmake'], 'type': 'language'},
        'leadership': {'category': 'Soft Skills', 'variations': ['leadership'], 'type': 'soft skill'},
        'digital marketing': {'category': 'Soft Skills', 'variations': ['digital marketing'], 'type': 'soft skill'},
        'communication': {'category': 'Soft Skills', 'variations': ['communication'], 'type': 'soft skill'},
        'teamwork': {'category': 'Soft Skills', 'variations': ['teamwork'], 'type': 'soft skill'},
        'problem solving': {'category': 'Soft Skills', 'variations': ['problem solving'], 'type': 'soft skill'},
        'time management': {'category': 'Soft Skills', 'variations': ['time management'], 'type': 'soft skill'},
        'adaptability': {'category': 'Soft Skills', 'variations': ['adaptability'], 'type': 'soft skill'},
        'creativity': {'category': 'Soft Skills', 'variations': ['creativity'], 'type': 'soft skill'},
        'critical thinking': {'category': 'Soft Skills', 'variations': ['critical thinking'], 'type': 'soft skill'},
        'work ethic': {'category': 'Soft Skills', 'variations': ['work ethic'], 'type': 'soft skill'},
        'interpersonal skills': {'category': 'Soft Skills', 'variations': ['interpersonal skills'], 'type': 'soft skill'},
        'public speaking': {'category': 'Soft Skills', 'variations': ['public speaking'], 'type': 'soft skill'},
        'emotional intelligence': {'category': 'Soft Skills', 'variations': ['emotional intelligence'], 'type': 'soft skill'},
        'conflict resolution': {'category': 'Soft Skills', 'variations': ['conflict resolution'], 'type': 'soft skill'},
        'decision making': {'category': 'Soft Skills', 'variations': ['decision making'], 'type': 'soft skill'},
        'networking': {'category': 'Soft Skills', 'variations': ['networking'], 'type': 'soft skill'},
        'collaboration': {'category': 'Soft Skills', 'variations': ['collaboration'], 'type': 'soft skill'},
        'analytical skills': {'category': 'Soft Skills', 'variations': ['analytical skills', 'analytical','analytics'], 'type': 'soft skill'},
        'Devops': {'category': 'Soft Skills', 'variations': ['devops'], 'type': 'soft skill'},
        'vuew': {'category': 'Soft Skills', 'variations': ['vuew'], 'type': 'soft skill'},
        'Django': {'category': 'Soft Skills', 'variations': ['Django'], 'type': 'soft skill'},
        'Express.js': {'category': 'Soft Skills', 'variations': ['Express.js','Express'], 'type': 'soft skill'},
        'Selenium': {'category': 'Soft Skills', 'variations': ['Selenium'], 'type': 'soft skill'},

        
        # Web Technologies
        'html': {'category': 'Web Technologies', 'variations': ['html', 'html5'], 'type': 'web'},
        'css': {'category': 'Web Technologies', 'variations': ['css', 'css3'], 'type': 'web'},
        'react': {'category': 'Frameworks & Libraries', 'variations': ['react', 'reactjs', 'react.js'], 'type': 'framework'},
        'angular': {'category': 'Frameworks & Libraries', 'variations': ['angular', 'angularjs'], 'type': 'framework'},
        'vue': {'category': 'Frameworks & Libraries', 'variations': ['vue', 'vuejs', 'vue.js'], 'type': 'framework'},
        'next.js': {'category': 'Frameworks & Libraries', 'variations': ['next.js', 'nextjs', 'next js'], 'type': 'framework'},
        'node.js': {'category': 'Frameworks & Libraries', 'variations': ['node.js', 'nodejs', 'node js'], 'type': 'framework'},
        'express': {'category': 'Frameworks & Libraries', 'variations': ['express', 'expressjs', 'express.js'], 'type': 'framework'},
        'django': {'category': 'Frameworks & Libraries', 'variations': ['django'], 'type': 'framework'},
        'flask': {'category': 'Frameworks & Libraries', 'variations': ['flask'], 'type': 'framework'},
        'jquery': {'category': 'Frameworks & Libraries', 'variations': ['jquery'], 'type': 'framework'},
        'bootstrap': {'category': 'Frameworks & Libraries', 'variations': ['bootstrap'], 'type': 'framework'},
        'tailwindcss': {'category': 'Frameworks & Libraries', 'variations': ['tailwind', 'tailwindcss', 'tailwind css'], 'type': 'framework'},
        'sass': {'category': 'Web Technologies', 'variations': ['sass', 'scss'], 'type': 'web'},
        'vite': {'category': 'Development Tools', 'variations': ['vite'], 'type': 'tool'},
        
        
        # Mobile Development
        'android': {'category': 'Mobile Development', 'variations': ['android'], 'type': 'mobile'},
        'ios': {'category': 'Mobile Development', 'variations': ['ios'], 'type': 'mobile'},
        'swiftui': {'category': 'Mobile Development', 'variations': ['swiftui', 'swift ui'], 'type': 'mobile'},
        'uikit': {'category': 'Mobile Development', 'variations': ['uikit', 'ui kit'], 'type': 'mobile'},
        'flutter': {'category': 'Mobile Development', 'variations': ['flutter'], 'type': 'mobile'},
        'react native': {'category': 'Mobile Development', 'variations': ['react native', 'react-native'], 'type': 'mobile'},
        
        # Databases
        'mysql': {'category': 'Databases', 'variations': ['mysql'], 'type': 'database'},
        'postgresql': {'category': 'Databases', 'variations': ['postgresql', 'postgres'], 'type': 'database'},
        'mongodb': {'category': 'Databases', 'variations': ['mongodb', 'mongo'], 'type': 'database'},
        'redis': {'category': 'Databases', 'variations': ['redis'], 'type': 'database'},
        'sqlite': {'category': 'Databases', 'variations': ['sqlite'], 'type': 'database'},
        'firebase': {'category': 'Databases', 'variations': ['firebase'], 'type': 'database'},
        'oracle': {'category': 'Databases', 'variations': ['oracle', 'oracle db'], 'type': 'database'},
        
        # Development Tools
        'git': {'category': 'Development Tools', 'variations': ['git'], 'type': 'tool'},
        'github': {'category': 'Development Tools', 'variations': ['github'], 'type': 'tool'},
        'gitlab': {'category': 'Development Tools', 'variations': ['gitlab'], 'type': 'tool'},
        'vscode': {'category': 'Development Tools', 'variations': ['vscode', 'visual studio code', 'vs code'], 'type': 'tool'},
        'docker': {'category': 'Development Tools', 'variations': ['docker'], 'type': 'tool'},
        'kubernetes': {'category': 'Development Tools', 'variations': ['kubernetes', 'k8s'], 'type': 'tool'},
        'postman': {'category': 'Development Tools', 'variations': ['postman'], 'type': 'tool'},
        'jenkins': {'category': 'Development Tools', 'variations': ['jenkins'], 'type': 'tool'},
        
        # Data Science & ML
        'tensorflow': {'category': 'Data Science & ML', 'variations': ['tensorflow'], 'type': 'ml'},
        'pytorch': {'category': 'Data Science & ML', 'variations': ['pytorch'], 'type': 'ml'},
        'scikit-learn': {'category': 'Data Science & ML', 'variations': ['scikit-learn', 'sklearn', 'scikit learn'], 'type': 'ml'},
        'pandas': {'category': 'Data Science & ML', 'variations': ['pandas'], 'type': 'ml'},
        'numpy': {'category': 'Data Science & ML', 'variations': ['numpy'], 'type': 'ml'},
        'matplotlib': {'category': 'Data Science & ML', 'variations': ['matplotlib'], 'type': 'ml'},
        'keras': {'category': 'Data Science & ML', 'variations': ['keras'], 'type': 'ml'},
        
        # Cybersecurity
        'nmap': {'category': 'Cybersecurity', 'variations': ['nmap', 'network scanning'], 'type': 'security'},
        'wireshark': {'category': 'Cybersecurity', 'variations': ['wireshark'], 'type': 'security'},
        'metasploit': {'category': 'Cybersecurity', 'variations': ['metasploit'], 'type': 'security'},
        'kali linux': {'category': 'Cybersecurity', 'variations': ['kali', 'kali linux'], 'type': 'security'},
        'burp suite': {'category': 'Cybersecurity', 'variations': ['burp suite', 'burp'], 'type': 'security'},
        'owasp': {'category': 'Cybersecurity', 'variations': ['owasp', 'oswap'], 'type': 'security'},
        'scapy': {'category': 'Cybersecurity', 'variations': ['scapy'], 'type': 'security'},
        'osint': {'category': 'Cybersecurity', 'variations': ['osint'], 'type': 'security'},
        'penetration testing': {'category': 'Cybersecurity', 'variations': ['penetration testing', 'pen testing', 'pentest'], 'type': 'security'},
        'ethical hacking': {'category': 'Cybersecurity', 'variations': ['ethical hacking', 'hacking'], 'type': 'security'},
        'bug bounty': {'category': 'Cybersecurity', 'variations': ['bug bounty hunting', 'bug bounty'], 'type': 'security'},
        
        # Cloud & Infrastructure
        'aws': {'category': 'Cloud & Infrastructure', 'variations': ['aws', 'amazon web services'], 'type': 'cloud'},
        'azure': {'category': 'Cloud & Infrastructure', 'variations': ['azure', 'microsoft azure'], 'type': 'cloud'},
        'gcp': {'category': 'Cloud & Infrastructure', 'variations': ['gcp', 'google cloud'], 'type': 'cloud'},
        
        # Hardware & Embedded
        'arduino': {'category': 'Hardware & Embedded', 'variations': ['arduino'], 'type': 'hardware'},
        'raspberry pi': {'category': 'Hardware & Embedded', 'variations': ['raspberry pi', 'raspi'], 'type': 'hardware'},
        
        # Data & Analytics
        'power bi': {'category': 'Data & Analytics', 'variations': ['power bi', 'powerbi'], 'type': 'analytics'},
        'tableau': {'category': 'Data & Analytics', 'variations': ['tableau'], 'type': 'analytics'},
        'excel': {'category': 'Data & Analytics', 'variations': ['excel', 'microsoft excel'], 'type': 'analytics'},
        'Microsoft Power BI': {'category': 'Data & Analytics', 'variations': ['microsoft power bi'], 'type': 'analytics'},
        'word': {'category': 'Data & Analytics', 'variations': ['word', 'microsoft word'], 'type': 'analytics'},
        'google analytics': {'category': 'Data & Analytics', 'variations': ['google analytics'], 'type': 'analytics'},
        'powerpoint': {'category': 'Data & Analytics', 'variations': ['powerpoint', 'microsoft powerpoint'], 'type': 'analytics'},
        # Machine Learning & AI
        'machine learning': {'category': 'Machine Learning & AI', 'variations': ['machine learning', 'ml'], 'type': 'ml'},
        'deep learning': {'category': 'Machine Learning & AI', 'variations': ['deep learning', 'dl'], 'type': 'ml'},
        'computer vision': {'category': 'Machine Learning & AI', 'variations': ['computer vision', 'cv'], 'type': 'ml'},
        
        # Others
        'data structures': {'category': 'Computer Science Fundamentals', 'variations': ['data structures', 'dsa'], 'type': 'cs'},
        'object-oriented programming': {'category': 'Computer Science Fundamentals', 'variations': ['object-oriented programming', 'oop'], 'type': 'cs'},
        'algorithms': {'category': 'Computer Science Fundamentals', 'variations': ['algorithms', 'algo'], 'type': 'cs'},
        'restful api': {'category': 'Web Technologies', 'variations': ['restful api', 'rest api', 'rest'], 'type': 'web'},
        'matlab': {'category': 'Development Tools', 'variations': ['matlab'], 'type': 'tool'},
        'cygwin': {'category': 'Development Tools', 'variations': ['cygwin'], 'type': 'tool'},
        'git extensions': {'category': 'Development Tools', 'variations': ['git extensions'], 'type': 'tool'},
        'postman': {'category': 'Development Tools', 'variations': ['postman'], 'type': 'tool'},
        'jenkins': {'category': 'Development Tools', 'variations': ['jenkins'], 'type': 'tool'},
    }

def format_skill_name(skill: str, skill_db: Dict) -> str:
    """
    Format skill name properly (capitalize, etc.)
    """
    formatting_map = {
        'python': 'Python',
        'java': 'Java',
        'javascript': 'JavaScript',
        'c': 'C',
        'c++': 'C++',
        'c#': 'C#',
        'html': 'HTML',
        'css': 'CSS',
        'sql': 'SQL',
        'php': 'PHP',
        'react': 'React',
        'angular': 'Angular',
        'vue': 'Vue.js',
        'node.js': 'Node.js',
        'next.js': 'Next.js',
        'mongodb': 'MongoDB',
        'postgresql': 'PostgreSQL',
        'mysql': 'MySQL',
        'git': 'Git',
        'github': 'GitHub',
        'vscode': 'VS Code',
        'ios': 'iOS',
        'android': 'Android',
        'swiftui': 'SwiftUI',
        'uikit': 'UIKit',
        'swift': 'Swift',
        'kotlin': 'Kotlin',
        'django': 'Django',
        'flask': 'Flask',
        'jquery': 'jQuery',
        'bootstrap': 'Bootstrap',
        'tailwindcss': 'TailwindCSS',
        'firebase': 'Firebase',
        'docker': 'Docker',
        'kubernetes': 'Kubernetes',
        'aws': 'AWS',
        'azure': 'Azure',
        'gcp': 'GCP',
        'arduino': 'Arduino',
        'nmap': 'NMAP',
        'owasp': 'OWASP',
        'scapy': 'Scapy',
        'osint': 'OSINT',
        'power bi': 'Power BI',
        'typescript': 'TypeScript',
        'scikit-learn': 'Scikit-learn',
        'pandas': 'Pandas',
        'numpy': 'NumPy',
        'tensorflow': 'TensorFlow',
        'pytorch': 'PyTorch',
        'data structures': 'Data Structures',
        'algorithms': 'Algorithms',
        'machine learning': 'Machine Learning',
        'deep learning': 'Deep Learning',
        'computer vision': 'Computer Vision',
        'natural language processing': 'Natural Language Processing',
        'cybersecurity': 'Cybersecurity',
        'network security': 'Network Security',
        'matplotlib': 'Matplotlib',
        'keras': 'Keras',
        'ethical hacking': 'Ethical Hacking',
        'penetration testing': 'Penetration Testing',
        'bug bounty': 'Bug Bounty Hunting',
        'restful api': 'RESTful API',
        'cygwin': 'Cygwin',
        'git extensions': 'Git Extensions',
        'matlab': 'MATLAB',
        'postman': 'Postman',
        'jenkins': 'Jenkins',
        'cmake': 'CMake',
    }
    
    return formatting_map.get(skill, skill.title())

QUALIFICATION_KEYWORDS = {
    # --- Core CS ---
    "computer science": "Computer Science",
    "computer science engineering": "Computer Science",
    "cse": "Computer Science",
    "bcs": "Computer Science",
    "b.sc cs": "Computer Science",
    "b.sc computer science": "Computer Science",
    "bachelor of computer application": "BCA",
    "bca": "BCA",
    "Master of Computer Applications": "MCA",
    "mca": "MCA",
    "any graduate": "Any Graduate",
    "any post graduate": "Any Post Graduate",


    # --- IT / Information Science ---
    "information technology": "Information Technology",
    "information science": "Information Science",
    "information science engineering": "Information Science",
    "ise": "Information Science",

    # --- AI / ML / DS ---
    "artificial intelligence": "AI ML",
    "ai": "AI ML",
    "machine learning": "AI ML",
    "ai and ml": "AI ML",
    "artificial intelligence and machine learning": "AI ML",
    "data science": "Data Science",
    "data analytics": "Data Science",

    # --- Business / Systems ---
    "computer science and business systems": "Business Systems",
    "csbs": "Business Systems",
    "business systems": "Business Systems",
    "information systems": "Business Systems",

    # --- Robotics / Automation (CS-related only) ---
    "computer and robotics": "Robotics",
    "robotics and automation": "Robotics",
    "robotics engineering": "Robotics",

    # --- Software / Computing Variants ---
    "software engineering": "Software Engineering",
    "software systems": "Software Engineering",

    # --- Electronics with CS overlap ---
    "electronics and computer engineering": "Electronics & Computing",
    "electronics and computing": "Electronics & Computing",
    "ece with computer science": "Electronics & Computing",
    "electronics and communication with cs": "Electronics & Computing",
    "electrical and computer engineering": "Electronics & Computing",
    "electrical and electronics ": "Electrical & Electronics",
    "electrical engineering": "Electrical Engineering",
    "electronics engineering": "Electronics Engineering",
    "communication engineering": "Communication Engineering",
    "embedded systems": "Embedded Systems",
    "embedded systems engineering": "Embedded Systems",
    "chemical engineering": "Chemical Engineering",


    # --- Cyber / Security ---
    "cyber security": "Cyber Security",
    "cybersecurity": "Cyber Security",
    "information security": "Cyber Security"
}

def extract_branch_from_resume_lines(resume_lines):
    # Join everything
    full_text = " ".join(resume_lines).lower()

    print("====== FULL TEXT ======")
    print(full_text)

    # HARD normalize (this is key)
    full_text = re.sub(r'[^a-z0-9 ]+', ' ', full_text)  # remove symbols
    full_text = re.sub(r'\s+', ' ', full_text)

    if "artificial intelligence" in full_text and "machine learning" in full_text:
        return "AI ML"

    if "computer science" in full_text or "information science" in full_text or "cloud computing" in full_text or "computer engineering" in full_text or "cse" in full_text or "computer science and business systems" in full_text or "csbs" in full_text:
        return "Computer Science"

    if "information technology" in full_text or "information science" in full_text:
        return "Information Technology"
    
    if "business systems" in full_text or "information systems" in full_text:
        return "Business Systems"
    
    if "data science" in full_text :
        return "Data Science"
    
    if "electronics and communication" in full_text:
        return "Electrical & Communication"

    if "electrical and electronics" in full_text or "electrical engineering" in full_text:
        return "Electrical & Electronics"
    
    if "cyber security" in full_text or "cybersecurity" in full_text:
        return "Cyber Security"
    if "mechanical engineering" in full_text:
        return "Mechanical Engineering" 
    
    if "civil engineering" in full_text:
        return "Civil Engineering"
    
    
    return "Any"

def get_skill_resources(skill: str) -> list:
    """
    Returns course links for a given skill.
    Each resource is a dict with 'title' and 'url'
    """
    resource_map = {
        "SQL and NoSQL": [
            {"title": "SQL Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
            {"title": "NoSQL Database Tutorial", "url": "https://www.youtube.com/watch?v=0buKQHokLK8"}
        ],
        "SQL": [
            {"title": "SQL Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
            {"title": "SQL for Beginners", "url": "https://www.youtube.com/watch?v=7S_tz1z_5bA"}
        ],
        "NoSQL": [
            {"title": "NoSQL Database Tutorial", "url": "https://www.youtube.com/watch?v=0buKQHokLK8"}
        ],
        "Git": [
            {"title": "Git & GitHub Tutorial - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=RGOj5yH7evk"},
            {"title": "Git for Beginners", "url": "https://www.youtube.com/watch?v=8JJ101D3knE"}
        ],
        "Power BI": [
            {"title": "Power BI Full Course", "url": "https://www.youtube.com/watch?v=AGrl-H87pRU"},
            {"title": "Power BI Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=77vXdROOY_g"}
        ],
        "JavaScript": [
            {"title": "JavaScript Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=PkZNo7MFNFg"},
            {"title": "JavaScript for Beginners", "url": "https://www.youtube.com/watch?v=W6NZfCO5SIk"}
        ],
        "Python": [
            {"title": "Python for Beginners - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw"},
            {"title": "Python Full Course", "url": "https://www.youtube.com/watch?v=8DvywoWv6gI"}
        ],
        "React": [
            {"title": "React JS Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=bMknfKXIFA8"},
            {"title": "React Tutorial", "url": "https://www.youtube.com/watch?v=SqcY0GlETPk"}
        ],
        "Angular": [
            {"title": "Angular Tutorial - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=3qBXWUpoPHo"},
            {"title": "Angular Full Course", "url": "https://www.youtube.com/watch?v=2OHbjep_WjQ"}
        ],
        "Node.js": [
            {"title": "Node.js Full Course", "url": "https://www.youtube.com/watch?v=Oe421EPjeBE"},
            {"title": "Node.js Tutorial", "url": "https://www.youtube.com/watch?v=TlB_eWDSMt4"}
        ],
        "MongoDB": [
            {"title": "MongoDB Tutorial - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=c2M-rlkkT5o"},
            {"title": "MongoDB Crash Course", "url": "https://www.youtube.com/watch?v=ofme2o29ngU"}
        ],
        "Docker": [
            {"title": "Docker Tutorial - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=pTFZFxd4hOI"},
            {"title": "Docker for Beginners", "url": "https://www.youtube.com/watch?v=fqMOX6JJhGo"}
        ],
        "Kubernetes": [
            {"title": "Kubernetes Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=X48VuDVv0do"},
            {"title": "Kubernetes Tutorial", "url": "https://www.youtube.com/watch?v=d6WC5n9G_sM"}
        ],
        "AWS": [
            {"title": "AWS Certified Solutions Architect", "url": "https://www.youtube.com/watch?v=Ia-UEYYR44s"},
            {"title": "AWS Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=k1RI5locZE4"}
        ],
        "Machine Learning": [
            {"title": "Machine Learning Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=Gv9_4yMHFhI"},
            {"title": "ML for Beginners", "url": "https://www.youtube.com/watch?v=i_LwzRVP7bg"}
        ],
        "Data Structures": [
            {"title": "Data Structures Full Course", "url": "https://www.youtube.com/watch?v=B31LgI4Y4DQ"},
            {"title": "Data Structures and Algorithms", "url": "https://www.youtube.com/watch?v=8hly31xKli0"}
        ],
        "Java": [
            {"title": "Java Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=xk4_1vDrzzo"},
            {"title": "Java Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=eIrMbAQSU34"}
        ],
        "C++": [
            {"title": "C++ Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=vLnPwxZdW4Y"},
            {"title": "C++ Tutorial", "url": "https://www.youtube.com/watch?v=8jLOx1hD3_o"}
        ],
        "C": [
            {"title": "C Programming Full Course", "url": "https://www.youtube.com/watch?v=KJgsSFOSQv0"},
            {"title": "C Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=87SH2Cn0s9A"}
        ],
        "HTML": [
            {"title": "HTML Full Course", "url": "https://www.youtube.com/watch?v=pQN-pnXPaVg"},
            {"title": "HTML Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=qz0aGYrrlhU"}
        ],
        "CSS": [
            {"title": "CSS Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=1Rs2ND1ryYc"},
            {"title": "CSS Tutorial", "url": "https://www.youtube.com/watch?v=yfoY53QXEnI"}
        ],
        "PHP": [
            {"title": "PHP Full Course", "url": "https://www.youtube.com/watch?v=OK_JCtrrv-c"},
            {"title": "PHP Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=a7_WFUlFS94"}
        ],
        "Django": [
            {"title": "Django Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=F5mRW0jo-U4"},
            {"title": "Django Tutorial", "url": "https://www.youtube.com/watch?v=rHux0gMZ3Eg"}
        ],
        "Flask": [
            {"title": "Flask Tutorial - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=Z1RJmh_OqeA"},
            {"title": "Flask for Beginners", "url": "https://www.youtube.com/watch?v=dam0GPOAvVI"}
        ],
        "Spring Boot": [
            {"title": "Spring Boot Tutorial", "url": "https://www.youtube.com/watch?v=9SGDpanrc8U"},
            {"title": "Spring Boot Full Course", "url": "https://www.youtube.com/watch?v=vtPkZShrvXQ"}
        ],
        "MySQL": [
            {"title": "MySQL Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY"},
            {"title": "MySQL Tutorial", "url": "https://www.youtube.com/watch?v=7S_tz1z_5bA"}
        ],
        "PostgreSQL": [
            {"title": "PostgreSQL Tutorial", "url": "https://www.youtube.com/watch?v=qw--VYLpxG4"},
            {"title": "PostgreSQL Course", "url": "https://www.youtube.com/watch?v=SpfIwlAYaKk"}
        ],
        "Redux": [
            {"title": "Redux Tutorial - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=CVpUuw9XSjY"},
            {"title": "Redux for Beginners", "url": "https://www.youtube.com/watch?v=poQXNp9ItL4"}
        ],
        "Vue.js": [
            {"title": "Vue.js Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=FXpIoQ_rT_c"},
            {"title": "Vue.js Tutorial", "url": "https://www.youtube.com/watch?v=1GNsWa_EZdw"}
        ],
        "TypeScript": [
            {"title": "TypeScript Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=30LWjhZzg50"},
            {"title": "TypeScript Tutorial", "url": "https://www.youtube.com/watch?v=BwuLxPH8IDs"}
        ],
        "Tableau": [
            {"title": "Tableau Full Course", "url": "https://www.youtube.com/watch?v=aHaOIvR00So"},
            {"title": "Tableau Tutorial for Beginners", "url": "https://www.youtube.com/watch?v=jj6-0cvcNEA"}
        ],
        "Excel": [
            {"title": "Excel Full Course - FreeCodeCamp", "url": "https://www.youtube.com/watch?v=Vl0H-qTclOg"},
            {"title": "Excel Tutorial", "url": "https://www.youtube.com/watch?v=rwbho0CgEAE"}
        ],
        "R": [
            {"title": "R Programming Tutorial", "url": "https://www.youtube.com/watch?v=_V8eKsto3Ug"},
            {"title": "R for Beginners", "url": "https://www.youtube.com/watch?v=fDRa82lxzaU"}
        ]
    }
    
    return resource_map.get(skill, [])
