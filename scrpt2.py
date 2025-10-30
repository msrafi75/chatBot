# from google import genai
import google.generativeai as genai
import streamlit as st

# Configure the API key (no need to create a 'client')
genai.configure(api_key="AIzaSyDQkC-zfZSRqKSuW5PSvLA-Fc1clGf4suM")

# Set up Streamlit UI
st.title("Talk to My First Agent")
st.write("This app demonstrates a conversational agent")

user_input = st.text_input("Ask a question:")

if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        # Create model instance
        model = genai.GenerativeModel("gemini-2.0-flash")  # or "gemini-2.0-flash" if available
        response = model.generate_content(user_input)
        
    st.write(response.text)