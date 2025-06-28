import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def summarize_text(text):
    prompt = f"Summarize the following legal text into bullet points and a flowchart:\n\n{text}\n\nSummary:"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a legal assistant that simplifies legal text into summary and flowchart."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
