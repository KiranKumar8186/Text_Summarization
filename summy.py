import streamlit as st
from rake_nltk import Rake
import nltk 
nltk.download('punkt')
from transformers import pipeline

# Helper function to create point-wise summary
def point_wise_summary(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=30)
    summary_text = summary[0]["summary_text"]
    points = summary_text.split(".")
    return [point + "." for point in points]
# Helper function to extract keywords
def extract_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()

# Streamlit app
st.title("Text Summarizer")

# Get user input
text = st.text_area("Enter your text here:")

# Add a button
if st.button("Summarize"):
    # Show summary
    if text:
        summary_points = point_wise_summary(text)
        st.write("Summary:")
        for point in summary_points:
            st.write("+ " + point)
        # Extract keywords
        keywords = extract_keywords(text)
        st.write("Keywords:")
        for keyword in keywords:
            st.write("+ " + keyword)
