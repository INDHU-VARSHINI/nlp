import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')  # ensures English tagger
text = "NLP lab exam is easy"
tokens = word_tokenize(text)
print("Before:", text)
print(nltk.pos_tag(tokens))
