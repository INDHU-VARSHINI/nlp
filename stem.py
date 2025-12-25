from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["playing", "played", "plays", "better", "running","ran"]
stemmed = [ps.stem(w) for w in words]
print("Stemmed Words:", stemmed)