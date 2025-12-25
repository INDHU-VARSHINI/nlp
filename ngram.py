import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download("punkt")

text = "data mining techquines extract useful patterns from large datasets"
tokens = word_tokenize(text)

print("N-grams Generation")
print("Before:", text)

for n in range(1, 4):
    n_grams = list(ngrams(tokens, n))
    print(f"\n{n}-gram output:")
    print(n_grams)
