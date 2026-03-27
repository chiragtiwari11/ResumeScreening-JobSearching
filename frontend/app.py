import streamlit as st
import requests

st.title("Resume Job Matcher AI 🚀")

file = st.file_uploader("Upload Resume")

if file:
    res = requests.post(
        "http://127.0.0.1:8000/api/v1/resume/upload",
        files={"file": file}
    )

    text = res.json()["resume_text"]

    match = requests.post(
        "http://127.0.0.1:8000/api/v1/match/",
        params={"resume_text": text}
    )

    st.write(match.json())