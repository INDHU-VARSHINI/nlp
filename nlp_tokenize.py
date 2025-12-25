import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt_tab')
sample_text = "This is a sentence. This is another one!\nAnd this is the last one."
tokens = word_tokenize(sample_text)
sentences = sent_tokenize(sample_text)
print("before: ", sample_text)
print("after word_tokenize:", tokens)
print("after sent_tokenize:", sentences)