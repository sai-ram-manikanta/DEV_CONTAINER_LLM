import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration for Google Generative AI
GOOGLE_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.title('LLM Model Draft v1.0')

text_input = st.text_area('Ask query here:')
submit = st.button('Generate Response')

if submit:
    response = model.generate_content(text_input)
    st.write(response.text)