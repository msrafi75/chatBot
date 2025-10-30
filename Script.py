from google import genai
import streamlit as st

client = genai.client(api_key='AIzaSyDQkC-zfZSRqKSuW5PSvLA-Fc1clGf4suM')

st.title("Talk to My First Agent")
st.write("This app demostrates a conversational agent")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is Thinking.."):
        response =client.models.generate_content(
            model = 'gemini-2.0-flash', contents=user_input
        )
    st.write(response.text)
    