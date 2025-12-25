from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
texts = [
    "I love this product",
    "This is bad",
    "It is okay",
    "Very good experience",
    "Worst service",
    "The movie was average"
]

labels = ["positive","negative","neutral","positive","negative","neutral"]

# Vectorization
X = CountVectorizer().fit_transform(texts)

# Model training
model = MultinomialNB()
model.fit(X, labels)

# Prediction
y_pred = model.predict(X)

# Confusion Matrix
cm = confusion_matrix(labels, y_pred, labels=["positive","negative","neutral"])
print("Confusion Matrix:\n", cm)

# Classification Report
print("\nClassification Report:\n",
      classification_report(labels, y_pred))

# Heatmap
sns.heatmap(cm, annot=True, cmap="Blues",
            xticklabels=["positive","negative","neutral"],
            yticklabels=["positive","negative","neutral"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
