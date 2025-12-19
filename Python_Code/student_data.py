from .Export_data import (
    extract_name_from_data,
    extract_skills_from_data,
    extract_data_from_pdf,
    clean_the_data,
    list_the_skills,
    clean_sentence_in_prefered_skills,
    extract_branch_from_qualification,
    extract_branch_from_resume
)
import json   
import pandas as pd
import re 

print(json.__file__)

def preprocess_resume(resume):
    """
    Read the resume here than extract data from resume
    then rectify the noise out of data then process other things
    Pdf -> export text -> clean text.

    """
    raw_text = extract_data_from_pdf(resume) 
    proper_text_data = clean_the_data(raw_text)

    return proper_text_data

def process_all_resume_data(user_pdf):
    """ 
    fetch the pdf data from front end and perform required operation and segrate 
    required data. 
    """
    pdf_data = preprocess_resume(user_pdf) 

    extract_name = extract_name_from_data(pdf_data)

    extract_skills = extract_skills_from_data(pdf_data)

    extract_branch = extract_branch_from_resume(pdf_data)

    #create json data to parse into c++ 

    resume_dict = {
        "candidate_info": {
            "Name": extract_name,
            "Branch": extract_branch
        },
        "Skills": extract_skills,
        #"Education": extract_education
    }
    file_path = "C:/research/PBL_DSA/parse_resume_data_to_cpp.json"
    
    with open(file_path, "w") as json_file:
        json.dump(resume_dict, json_file, indent = 4)

    print("JSON file created successfully.")
     # You can process company_dict as needed
    file_path_company = "C:/research/PBL_DSA/company_job_data_to_cpp.json"
    company_list , qualification, skill_list, preferred_Skill, role_list = extract_company_data()

    company_data = []
    
    for company , qual , skill , pref_skill , role in zip(company_list , qualification, skill_list, preferred_Skill, role_list):
        company_dict = {
            "Company":company,
            "Qualification": extract_branch_from_qualification(qual),
            "Skills":list_the_skills(skill),
            "Preferred Skills":clean_sentence_in_prefered_skills(pref_skill),
            "Role":role
        }
        company_data.append(company_dict)     

    with open(file_path_company , "w") as json_file:
            json.dump(company_data , json_file , indent =4 )

    return extract_skills


def extract_company_data():
    df = pd.read_excel('C:/research/PBL_DSA/company_job_data_list.xlsx')
    company_list = df['Company'].tolist()
    qualification = df['Qualification'].tolist()
    skill_list = df['Skills'].tolist()
    preferred_Skill = df['Preferred Skills'].tolist()
    role_list = df['Role'].tolist()
    return company_list , qualification, skill_list, preferred_Skill, role_list
