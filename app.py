import streamlit as st
from utils.fetch_web_act import get_bare_act_text
from utils.extract_text import extract_pdf_text
from utils.summarizer import summarize_text
from utils.visualizer import generate_flowchart

st.set_page_config(layout="wide", page_title="Bare Act Summarizer")

st.title("📜 Bare Act Summarizer with AI")

option = st.radio("Choose input type", ["Text Input", "PDF Upload"])

text = ""
if option == "Text Input":
    act_name = st.text_input("Enter the name of the Bare Act")
    section_input = st.text_input("Enter Section No./Name")
    if act_name and section_input:
        with st.spinner("Fetching and processing the act..."):
            text = get_bare_act_text(act_name, section_input)
elif option == "PDF Upload":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        with st.spinner("Reading uploaded PDF..."):
            text = extract_pdf_text(uploaded_file)

if text:
    with st.spinner("Summarizing using AI..."):
        summary = summarize_text(text)
        st.subheader("Summary:")
        st.write(summary)

        st.subheader("Flowchart:")
        fig = generate_flowchart(summary)
        st.graphviz_chart(fig)
