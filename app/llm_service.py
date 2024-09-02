# app/llm_service.py

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load openai_key
load_dotenv()  # loads the .env file
api_key = os.getenv('api_key')

def llm_generate(input):
    # Load openai_key
    load_dotenv()  # loads the .env file
    api_key = os.getenv('api_key')

    genai.configure(api_key= api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text
