import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
from Python_Code import student_data

st.set_page_config(page_title="Student Resume Analyzer", layout="centered")

st.title("Student Resume Analyzer 🎓")
st.markdown("Upload your resume in PDF format here 👇")

data = None

with st.container():
    uploaded_file = st.file_uploader(
        label="",
        type=["pdf"],
        help="Upload your resume in PDF format only"
    )

    button_clicked = st.button("Parse Resume")  # ✅ only once

if button_clicked:
    if uploaded_file is None:
        st.warning("Please upload a PDF file to proceed. ⚠️")

    elif not uploaded_file.name.lower().endswith(".pdf"):
        st.error("Invalid file format! Please upload a PDF file. ❌")

    else:
        data = student_data.process_all_resume_data(uploaded_file)
        st.success("Resume uploaded successfully! ✅")

        if data:
            st.write(f"Pdf data is {data}")
        else:
            st.error("Could not extract data from the resume. ❌")
