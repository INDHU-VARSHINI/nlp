import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop=set(stopwords.words("english"))
text = "python is a popular programming language that is widely used for data analysis"
clean = " ".join([w for w in text.split() if w not in stop])
print("Before Removing Stop Words:", text)
print("After Removing Stop Words:", clean)
