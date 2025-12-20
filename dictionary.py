 # Simple Dictionary Program

dictionary = {
    "algorithm": "A step-by-step procedure for solving a proglem",
    "computer": "An electronic device that process data",
    "variable": "A storage location used to hold data",
    "function": "A block of code that performs a specific task",
    "natural": "Existing in nature, not artificail",
    "transform": "To change something completely",
    "radiant": "Giving off light or heat",
    "genuine": "Real or authenic",
    "enhance": "To improve or increase something",
    "glow": "A warm and attractive light or color",
    "cosmetics": "Products used to enhance one's appearance",
    "flawless": "Completely free from imperfections",
    "gigabyte": "A unit of information stored in a computer",
    "duplicate": "Have two corresponding parts, one of two identical things",
    "equivalent": "Equal i value, amount, meaning, etc",
    "inefficitive": "Failing to make the best use of time or resoures",
    "inexpensive": "Not costing a great deal",
    "residence": "The fact of living somewhere",
    "frequency": "The rate at which something occurs in a givien period or sample",
    "cyber": "Relating to information technology, the internet,and virtual reality"
    }

word = input("Enter a word: ").lower()
  
if word in dictionary:
    print(f"Meaning: {dictionary[word]}")
else:
    print("word not found in dictionary.")
     
    