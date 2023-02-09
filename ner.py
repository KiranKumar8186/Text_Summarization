import streamlit as st
import spacy
import altair as alt
import pandas as pd

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_sm")

# Add a title and some instructions to the page
st.title("Named Entity Recognition")
st.markdown("---")
# Create a Streamlit text input widget
text = st.text_area("Text:")

# Add a submit button
if st.button("Submit"):
    # Use the NER model to extract entities from the text
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    # Create a dataframe from the entities
    df = pd.DataFrame(entities, columns=["Entity", "Label"])

    st.table(df)
