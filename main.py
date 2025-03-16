import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
from streamlit_clerk_auth import clerk_login

# Initialize Firebase
cred = credentials.Certificate("path/to/firebase-key.json")  # Replace with your Firebase key file
firebase_admin.initialize_app(cred)
db = firestore.client()

# Configure Google Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your API key

# Streamlit UI
st.title("🎤 AI Mock Interview Platform")
st.subheader("Practice job interviews with AI-powered responses")

# Clerk Authentication
user = clerk_login()

if user:
    st.write(f"👋 Welcome, {user['first_name']}!")

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

else:
    st.warning("Please log in to use the platform.")


