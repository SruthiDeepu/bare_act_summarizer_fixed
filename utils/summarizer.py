import streamlit as st
from openai import OpenAI
from openai import RateLimitError

# Initialize OpenAI client with your secret API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def summarize_text(text):
    prompt = f"Summarize the following legal text into bullet points and a flowchart:\n\n{text}\n\nSummary:"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using gpt-3.5-turbo for better availability
            messages=[
                {"role": "system", "content": "You are a legal assistant that simplifies legal text into summary and flowchart."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content

    except RateLimitError:
        return "⚠️ OpenAI rate limit exceeded. Please try again later."
