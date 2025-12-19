from .Export_data import (
    extract_name_from_data,
    extract_skills_from_data,
    extract_data_from_pdf,
    clean_the_data
)
import json        

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

    #create json data to parse into c++ 

    resume_dict = {
        "candidate_info": {
            "Name": extract_name,
        },
        "Skills": extract_skills,
        #"Education": extract_education
    }
    file_path = "C:/research/PBL_DSA/parse_resume_data_to_cpp.json"
    
    with open(file_path, "w") as json_file:
        json.dump(resume_dict, json_file, indent = 4)

    print("JSON file created successfully.")

    return extract_skills


