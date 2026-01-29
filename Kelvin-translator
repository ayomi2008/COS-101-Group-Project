import streamlit as st
from translations import translations

st.set_page_config(page_title="Multi-Language Dictionary", page_icon="🌍")

st.title("🌍 Multi-Language Dictionary")
st.write("Translate 20 English words into 5 languages")

word = st.text_input("Enter an English word").lower()

language = st.selectbox(
    "Choose a language",
    ["french", "spanish", "german", "yoruba", "igbo"]
)

if st.button("Translate"):
    result = translations.get(word, {}).get(language)

    if result:
        st.success(f"**Translation:** {result}")
    else:
        st.error("Word or language not found")