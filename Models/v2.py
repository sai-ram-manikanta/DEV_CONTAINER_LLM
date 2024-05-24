import streamlit as st
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration for Google Generative AI
GOOGLE_API_KEY = os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Streamlit app title
st.title('LLM Model Draft v1.0')

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