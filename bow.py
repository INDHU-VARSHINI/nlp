from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
texts = ["I love NLP", "NLP lab is easy", "I love lab work"]
X = vectorizer.fit_transform(texts)
print("Vocabulary:", vectorizer.get_feature_names_out())
print("Bag of Words Array:\n", X.toarray())
