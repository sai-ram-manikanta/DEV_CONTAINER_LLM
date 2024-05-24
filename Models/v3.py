import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration for Google Generative AI
GOOGLE_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Streamlit app title
st.title('LLM Model Draft v1.0')

# High-contrast mode toggle
high_contrast = st.checkbox('Enable high-contrast mode')

# Custom CSS for high-contrast mode
high_contrast_css = """
<style>
body {
    background-color: #000000;
    color: #FFFFFF;
}
h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF;
}
.stButton>button {
    background-color: #FFFFFF;
    color: #000000;
    border: 2px solid #FFFFFF;
}
.stTextArea textarea {
    background-color: #333333;
    color: #FFFFFF;
}
.stFileUploader>label {
    color: #FFFFFF;
}
.stDataFrame {
    background-color: #333333;
    color: #FFFFFF;
}
</style>
"""

# Apply high-contrast CSS if the checkbox is checked
if high_contrast:
    st.markdown(high_contrast_css, unsafe_allow_html=True)

# File uploader widget to upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file using pandas
    data = pd.read_csv(uploaded_file)
    
    # Display the data
    st.write("Data:")
    st.write(data)
    
    # Generate summary statistics
    summary = data.describe(include='all')
    
    # Display the summary
    st.write("Summary:")
    st.write(summary)
    
    # Generate a text summary of the data
    st.write("Generating text summary of the data...")
    text_summary_query = f"Provide a summary for the following dataset:\n{summary.to_string()}"
    text_summary_response = model.generate_content(text_summary_query)
    text_summary = text_summary_response.text
    
    # Display the text summary
    st.write("Text Summary:")
    st.write(text_summary)
    
    # Optionally, let the user generate a text summary of the data with their own query
    text_input = st.text_area('Ask query here:')
    submit = st.button('Generate Response')
    
    if submit:
        # Combine the data description into a single string to pass to the model
        query = text_input + "\n\nData Description:\n" + summary.to_string()
        
        # Generate response using the generative model
        response = model.generate_content(query)
        st.write(response.text)