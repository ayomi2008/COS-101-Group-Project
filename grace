word = {
    "clothes": {
        "idoma": "abo",
        "tiv": "abo",
        "hausa": "tufafi",
        "igbo": "uwe",
        "italian": "vestiti"
    },
    "money": {
        "idoma": "ishima",
        "tiv": "kudi",
        "hausa": "kudi",
        "igbo": "ego",
        "italian": "denaro"
    },
    "read": {
        "idoma": "ka",
        "tiv": "kor",
        "hausa": "karanta",
        "igbo": "guo",
        "italian": "leggere"
    },
    "family": {
        "idoma": "ufia",
        "tiv": "ityo",
        "hausa": "iyali",
        "igbo": "ezinụlọ",
        "italian": "famiglia"
    },

    # 🔽 15 MORE WORDS
    "water": {
        "idoma": "ami",
        "tiv": "mngu",
        "hausa": "ruwa",
        "igbo": "mmiri",
        "italian": "acqua"
    },
    "house": {
        "idoma": "oku",
        "tiv": "tar",
        "hausa": "gida",
        "igbo": "ụlọ",
        "italian": "casa"
    },
    "school": {
        "idoma": "skuul",
        "tiv": "skuul",
        "hausa": "makaranta",
        "igbo": "akwụkwọ",
        "italian": "scuola"
    },
    "book": {
        "idoma": "buku",
        "tiv": "buku",
        "hausa": "littafi",
        "igbo": "akwụkwọ",
        "italian": "libro"
    },
    "mother": {
        "idoma": "ina",
        "tiv": "mama",
        "hausa": "uwa",
        "igbo": "nne",
        "italian": "madre"
    },
    "father": {
        "idoma": "opa",
        "tiv": "papa",
        "hausa": "uba",
        "igbo": "nna",
        "italian": "padre"
    },
    "child": {
        "idoma": "ono",
        "tiv": "wan",
        "hausa": "yaro",
        "igbo": "nwa",
        "italian": "bambino"
    },
    "market": {
        "idoma": "ojogbo",
        "tiv": "mkase",
        "hausa": "kasuwa",
        "igbo": "ahịa",
        "italian": "mercato"
    },
    "eat": {
        "idoma": "nyam",
        "tiv": "yam",
        "hausa": "ci",
        "igbo": "rie",
        "italian": "mangiare"
    },
    "drink": {
        "idoma": "mu",
        "tiv": "nyor",
        "hausa": "sha",
        "igbo": "ṅụọ",
        "italian": "bere"
    },
    "go": {
        "idoma": "lo",
        "tiv": "ya",
        "hausa": "je",
        "igbo": "gaa",
        "italian": "andare"
    },
    "come": {
        "idoma": "wa",
        "tiv": "ya",
        "hausa": "zo",
        "igbo": "bia",
        "italian": "venire"
    },
    "sleep": {
        "idoma": "ngun",
        "tiv": "kpen",
        "hausa": "yi barci",
        "igbo": "rahụ",
        "italian": "dormire"
    },
    "work": {
        "idoma": "kpa",
        "tiv": "kpa",
        "hausa": "aiki",
        "igbo": "ọrụ",
        "italian": "lavoro"
    }
}
word = input("Enter a word: ").lower()
language = input("Enter a language: ").lower()

if word in word:
    if language in word[word]:
        print(words[word][language])
    else:
        print("Language not available")
else:
    print("Word not found")