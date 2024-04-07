import streamlit as st

st.title('Hello, Streamlit!')

text = st.text_area('Enter some text')
submit = st.button('Generate SQL Query')