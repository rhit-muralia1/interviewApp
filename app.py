import streamlit as st

def main():
    st.title("Interview Preparation App")
    st.write("Welcome to the Interview Preparation App! Here you can practice coding questions, review concepts, and track your progress.")

    role = st.selectbox("Select your role:", ["Electrical Engineer"])
    interview_type = st.selectbox("Select interview type:", ["Technical", "Behavioral"])

    if st.button("Start Interview Preparation"):
        st.write(f"You have selected the role: {role} and interview type: {interview_type}.")

    if st.button("Generate Question"):
        st.write("Generating a question for you...")
        st.write("Question: Explain the difference between AC and DC current.")
