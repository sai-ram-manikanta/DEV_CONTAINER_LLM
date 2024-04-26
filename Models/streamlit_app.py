import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyBrWhFNp-QDj3yAjJbW7-ukgqoRYO2-vL4'

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.title('LLM Model Draft v1.0')

text_input = st.text_area('Ask query here:')
submit = st.button('Generate Response')

if submit:
    response = model.generate_content(text_input)
    st.write(response.text)