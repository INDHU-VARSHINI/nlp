import nltk
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
words = ["playing", "played", "plays", "running", "studying"]
lemmas = [lemmatizer.lemmatize(w, pos='v') for w in words]
print("Before Words:", words)
print("Lemmatized Words:", lemmas)