import streamlit as st
import time
import os
from tempfile import NamedTemporaryFile
from summarizer import TransformerSummarizer

st.title("Text Summarization")
st.markdown("---")
# Upload audio file with streamlit
text_files = st.text_area("Type Text Here...")
#-------------------------------------------------------------------------------------------------------------------------

GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")

if st.button('Summarize Text'):
    with st.spinner('Model Loading'):
        time.sleep(3)
    st.success('Model Loaded')

    if text_files is not None:
        Summary = ''.join(GPT2_model(text_files, min_length=60))
        st.markdown(f'<p style="padding: 10px; text-align: left; color:black; background:#FFFACD ; font-size:15px; margin : 15px auto;">{Summary}</p>', unsafe_allow_html=True)
        st.success('Summarization Completed')
        st.download_button('Download', Summary, 'Summaryt.txt')
    else:
        st.error('Please Upload An Audio File')

#-------------------------------------------------------------------------------------------------------------------------
