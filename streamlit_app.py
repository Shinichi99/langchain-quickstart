import streamlit as st
from langchain_community.llms import OpenAI  # Import OpenAI from langchain-community

# Set up the page configuration
st.set_page_config(page_title="🦜🔗 Quickstart App")
st.title('🦜🔗 Quickstart App')

# Get OpenAI API key from the sidebar
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text, api_key):
    # Create an OpenAI instance
    llm = OpenAI(temperature=0.7, openai_api_key=api_key)
    # Get the response and display it
    response = llm(input_text)
    st.info(response)

with st.form('my_form'):
    # Create a text area and submit button
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    
    # Check if the API key is valid
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter a valid OpenAI API key!', icon='⚠')
    
    # Process the form submission
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text, openai_api_key)
