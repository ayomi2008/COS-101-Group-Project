# Multi-Language Translation Program
# Translates 20 English words into Hausa, Yoruba, Igbo, Japanese, and Chinese

def display_available_words():
    """Display all 20 available words"""
    print("\n" + "="*50)
    print("AVAILABLE WORDS FOR TRANSLATION")
    print("="*50)
    words = [
        'trousers', 'hair', 'shirt', 'skirt', 'book',
        'class', 'home', 'room', 'bed', 'sit',
        'stand up', 'go', 'come', 'run', 'jump',
        'sorry', 'shoes', 'head', 'hand', 'clock'
    ]
    
    for i in range(0, len(words), 5):
        row = words[i:i+5]
        print("  ".join(f"{word:12}" for word in row))
    print("="*50)

def display_menu():
    """Display the language selection menu"""
    print("\n" + "="*50)
    print("SELECT A TRANSLATION LANGUAGE")
    print("="*50)
    print("1. English to Hausa")
    print("2. English to Yoruba")
    print("3. English to Igbo")
    print("4. English to Japanese")
    print("5. English to Chinese")
    print("Q. Exit")
    print("="*50)

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

def translate_word(word, language_key, language_name):
    """Translate a single word and display with definition"""
    translations = get_translations()
    
    word = word.lower().strip()
    
    if word in translations:
        translation = translations[word][language_key]
        definition = translations[word]['definition']
        
        print("\n" + "="*50)
        print(f"TRANSLATION: {word.upper()} (English to {language_name})")
        print("="*50)
        print(f"\n{word} -> {translation}")
        print(f"(Definition: {definition})")
        print("\n" + "="*50)
    else:
        print(f"\nSorry, '{word}' is not in the available words list.")
        print("Please check the available words and try again.")

def main():
    """Main program loop"""
    # Display available words at the start
    display_available_words()
    
    language_map = {
        '1': ('hausa', 'Hausa'),
        '2': ('yoruba', 'Yoruba'),
        '3': ('igbo', 'Igbo'),
        '4': ('japanese', 'Japanese'),
        '5': ('chinese', 'Chinese')
    }
    
    current_language = None
    current_language_name = None
    
    while True:
        # If no language selected, show language menu
        if current_language is None:
            display_menu()
            choice = input("\nEnter your choice (1-5 or Q to quit): ").strip().lower()
            
            if choice == 'q':
                print("\nThank you for using the Multi-Language Translator!")
                print("Goodbye!")
                break
            elif choice in language_map:
                current_language, current_language_name = language_map[choice]
                print(f"\n✓ Selected: English to {current_language_name}")
            else:
                print("\nInvalid choice! Please enter 1-5 or Q to quit.")
                input("\nPress Enter to continue...")
        else:
            # Language already selected, ask for word to translate
            print(f"\n[Current Language: English to {current_language_name}]")
            word_input = input("\nEnter a word to translate (or 'back' to change language, 'q' to quit): ").strip().lower()
            
            if word_input == 'q':
                print("\nThank you for using the Multi-Language Translator!")
                print("Goodbye!")
                break
            elif word_input == 'back':
                current_language = None
                current_language_name = None
            else:
                translate_word(word_input, current_language, current_language_name)
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()