import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/translate"

st.set_page_config(page_title="Language Translator", layout="centered")

st.title("Transformer Language Translator")
# st.write("Enter English text and select target language:")

input_text = st.text_area("English Text", height=150)

col1, col2 = st.columns(2)

target_lang = None

with col1:
    if st.button("Translate to Hindi"):
        target_lang = "hi"

with col2:
    if st.button("Translate to French"):
        target_lang = "fr"

if target_lang and input_text.strip() != "":
    payload = {
        "text": input_text,
        "target_lang": target_lang
    }

    with st.spinner("Translating..."):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.subheader("Translated Output")
        st.success(result["translation"])
    else:
        st.error("Error from backend: " + response.text)
