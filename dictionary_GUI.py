import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Multi-Language Translator",
    page_icon="🌍"
)

def get_translations():
    """Return dictionary with all translations"""
    translations = {
        'trousers': {
            'hausa': 'wando',
            'yoruba': 'ṣòkòtò',
            'igbo': 'ogologo uwe',
            'japanese': 'ズボン (zubon)',
            'chinese': '裤子 (kùzi)',
            'definition': 'A piece of clothing worn on the legs'
        },
        'hair': {
            'hausa': 'gashi',
            'yoruba': 'irun',
            'igbo': 'ntutu',
            'japanese': '髪 (kami)',
            'chinese': '头发 (tóufa)',
            'definition': 'Strands that grow on the head'
        },
        'shirt': {
            'hausa': 'riga',
            'yoruba': 'ṣẹ́ẹ̀tì',
            'igbo': 'uwe elu',
            'japanese': 'シャツ (shatsu)',
            'chinese': '衬衫 (chènshān)',
            'definition': 'A garment worn on the upper body'
        },
        'skirt': {
            'hausa': 'siket',
            'yoruba': 'ìbòrun',
            'igbo': 'uwe mwada',
            'japanese': 'スカート (sukāto)',
            'chinese': '裙子 (qúnzi)',
            'definition': 'A garment that hangs from the waist'
        },
        'book': {
            'hausa': 'littafi',
            'yoruba': 'ìwé',
            'igbo': 'akwụkwọ',
            'japanese': '本 (hon)',
            'chinese': '书 (shū)',
            'definition': 'A written work with pages for reading'
        },
        'class': {
            'hausa': 'aji',
            'yoruba': 'kíláàsì',
            'igbo': 'klaasi',
            'japanese': '授業 (jugyō)',
            'chinese': '课堂 (kètáng)',
            'definition': 'A group of students learning together'
        },
        'home': {
            'hausa': 'gida',
            'yoruba': 'ilé',
            'igbo': 'ụlọ',
            'japanese': '家 (ie)',
            'chinese': '家 (jiā)',
            'definition': 'The place where you live'
        },
        'room': {
            'hausa': 'daki',
            'yoruba': 'yàrá',
            'igbo': 'ọnụ ụlọ',
            'japanese': '部屋 (heya)',
            'chinese': '房间 (fángjiān)',
            'definition': 'A space within a building'
        },
        'bed': {
            'hausa': 'gado',
            'yoruba': 'ibùsùn',
            'igbo': 'akwa',
            'japanese': 'ベッド (beddo)',
            'chinese': '床 (chuáng)',
            'definition': 'Furniture used for sleeping'
        },
        'sit': {
            'hausa': 'zauna',
            'yoruba': 'jókòó',
            'igbo': 'nọdụ ala',
            'japanese': '座る (suwaru)',
            'chinese': '坐 (zuò)',
            'definition': 'To rest on your bottom'
        },
        'stand up': {
            'hausa': 'tashi',
            'yoruba': 'dìde',
            'igbo': 'kwụrụ ọtọ',
            'japanese': '立つ (tatsu)',
            'chinese': '站起来 (zhàn qǐlái)',
            'definition': 'To rise to an upright position'
        },
        'go': {
            'hausa': 'tafi',
            'yoruba': 'lọ',
            'igbo': 'gaa',
            'japanese': '行く (iku)',
            'chinese': '去 (qù)',
            'definition': 'To move from one place to another'
        },
        'come': {
            'hausa': 'zo',
            'yoruba': 'wá',
            'igbo': 'bịa',
            'japanese': '来る (kuru)',
            'chinese': '来 (lái)',
            'definition': 'To move toward someone or something'
        },
        'run': {
            'hausa': 'gudu',
            'yoruba': 'sáré',
            'igbo': 'gbaa ọsọ',
            'japanese': '走る (hashiru)',
            'chinese': '跑 (pǎo)',
            'definition': 'To move quickly on foot'
        },
        'jump': {
            'hausa': 'tsalle',
            'yoruba': 'fò',
            'igbo': 'wụlie',
            'japanese': '跳ぶ (tobu)',
            'chinese': '跳 (tiào)',
            'definition': 'To push off the ground with your feet'
        },
        'sorry': {
            'hausa': 'yi hakuri',
            'yoruba': 'má bínú',
            'igbo': 'ndo',
            'japanese': 'ごめんなさい (gomennasai)',
            'chinese': '对不起 (duìbùqǐ)',
            'definition': 'An expression of apology or regret'
        },
        'shoes': {
            'hausa': 'takalma',
            'yoruba': 'bàtà',
            'igbo': 'akpụkpọ ụkwụ',
            'japanese': '靴 (kutsu)',
            'chinese': '鞋子 (xiézi)',
            'definition': 'Footwear that covers and protects the feet'
        },
        'head': {
            'hausa': 'kai',
            'yoruba': 'orí',
            'igbo': 'isi',
            'japanese': '頭 (atama)',
            'chinese': '头 (tóu)',
            'definition': 'The upper part of the body containing the brain'
        },
        'hand': {
            'hausa': 'hannu',
            'yoruba': 'ọwọ́',
            'igbo': 'aka',
            'japanese': '手 (te)',
            'chinese': '手 (shǒu)',
            'definition': 'The body part at the end of the arm'
        },
        'clock': {
            'hausa': 'agogo',
            'yoruba': 'aago',
            'igbo': 'elekere',
            'japanese': '時計 (tokei)',
            'chinese': '钟 (zhōng)',
            'definition': 'A device that shows the time'
        }
    }
    return translations

# Title
st.title("Multi-Language Translator")

# Sidebar
st.sidebar.header("Available Words")
translations = get_translations()
words_list = sorted(translations.keys())
for word in words_list:
    st.sidebar.write(f"• {word}")

# Language selection
language = st.selectbox(
    "Select Target Language:",
    ["Hausa", "Yoruba", "Igbo", "Japanese", "Chinese"]
)

language_key = language.lower()

# Word input
word_input = st.text_input("Enter an English word:")

# Translate button
if st.button("Translate"):
    if word_input:
        word = word_input.lower().strip()
        
        if word in translations:
            translation = translations[word][language_key]
            definition = translations[word]['definition']
            
            st.success(f"**{word}** → **{translation}**")
            st.info(f"Definition: {definition}")
        else:
            st.error(f"'{word}' is not available. Check the sidebar for available words.")
    else:
        st.warning("Please enter a word to translate.")