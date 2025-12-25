import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from operator import itemgetter
nltk.download("punkt")
nltk.download("stopwords")
doc = """I am a graduate. I want to learn Python. I like learning Python.
Python is easy. Python is interesting."""
# Sentences
sentences = sent_tokenize(doc)
print("Total sentences:", len(sentences))
# Words (KEEP stopwords for total count)
words = [w.lower() for w in word_tokenize(doc) if w.isalpha()]
print("Total words:", len(words))   # ✅ 22
# Stopwords
stop_words = set(stopwords.words("english"))
# TF
tf = {}
for w in words:
    if w not in stop_words:
        tf[w] = tf.get(w, 0) + 1
for w in tf:
    tf[w] /= len(words)

print("\nTF Score:")
print(tf)
# IDF
def sent_count(word):
    return sum(word in s.lower() for s in sentences)
idf = {}
for w in tf:
    idf[w] = math.log(len(sentences) / sent_count(w))
print("\nIDF Score:")
print(idf)
# TF-IDF
tf_idf = {w: tf[w] * idf[w] for w in tf}
print("\nTF-IDF Score:")
print(tf_idf)
# Top 5 keywords
top5 = dict(sorted(tf_idf.items(), key=itemgetter(1), reverse=True)[:5])
print("\nTop 5 Keywords:")
print(top5)