# English – Igbo Dictionary
# Programming language: Python
# Dictionary languages: English and Igbo

dictionary = {
    "algorithm": {
        "english": "A step-by-step procedure for solving a problem",
        "igbo": "Usoro nzọụkwụ site na nzọụkwụ iji dozie nsogbu"
    },
    "computer": {
        "english": "An electronic device that processes data",
        "igbo": "Ngwa eletrọnik nke na-ahazi data"
    },
    "variable": {
        "english": "A storage location used to hold data",
        "igbo": "Ebe a na-edobe ozi n’ime mmemme"
    },
    "function": {
        "english": "A block of code that performs a specific task",
        "igbo": "Akụkụ koodu nke na-arụ otu ọrụ"
    },
    "natural": {
        "english": "Existing in nature, not artificial",
        "igbo": "Ihe dị adị n’okike, ọ bụghị nke mmadụ mere"
    },
    "transform": {
        "english": "To change something completely",
        "igbo": "Ịgbanwe ihe kpamkpam"
    },
    "radiant": {
        "english": "Giving off light or heat",
        "igbo": "Na-enwu ma ọ bụ na-ewepụta okpomọkụ"
    },
    "genuine": {
        "english": "Real or authentic",
        "igbo": "Ezigbo ma ọ bụ nke bụ eziokwu"
    },
    "enhance": {
        "english": "To improve or increase something",
        "igbo": "Ime ka ihe ka mma"
    },
    "frequency": {
        "english": "The rate at which something occurs",
        "igbo": "Ugboro ole ihe na-eme n’oge"
    },
    "cyberspace": {
    "english": "The virtual environment of computer networks",
    "igbo": "Ụwa dijitalụ nke netwọkụ kọmputa"
},
    "network": {
    "english": "A group of interconnected computers or devices",
    "igbo": "Òtù kọmputa ma ọ bụ ngwaọrụ jikọrọ ọnụ"
}
}

word = input("Enter an English word: ").lower()

if word in dictionary:
    print("English meaning:", dictionary[word]["english"])
    print("Igbo meaning:", dictionary[word]["igbo"])
else:
    print("Word not found in dictionary.")
     

    
