import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Firebase
cred = credentials.Certificate("path/to/firebase-key.json")  # Replace with your actual Firebase key file
firebase_admin.initialize_app(cred)
db = firestore.client()

# Configure Google Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual API key

# Streamlit UI
st.title("🎤 AI Mock Interview Platform")
st.subheader("Practice job interviews with AI-powered responses")

# User Authentication with Firebase
user_email = st.text_input("Enter your email:")
user_password = st.text_input("Enter your password:", type="password")

if st.button("Login"):
    try:
        user = auth.get_user_by_email(user_email)
        st.success(f"Welcome, {user.display_name}!")
    except Exception as e:
        st.error("Invalid credentials. Please try again.")

# Input field for user question
user_question = st.text_input("Ask an interview question:", "")

if st.button("Get AI Response"):
    if user_question:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_question)
        st.write("🧠 AI Response:")
        st.write(response.text)
    else:
        st.warning("Please enter a question.")

