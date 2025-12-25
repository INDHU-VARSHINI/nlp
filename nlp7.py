import string
text = "Artificial intelligence is transforming the world by automating tasks"
# Preprocess
text = text.lower().translate(str.maketrans("", "", string.punctuation))
words = text.split()
# Create bigram dictionary
bigram = {words[i]: words[i+1] for i in range(len(words)-1)}
# Predict next words
def predict(start, n=7):
    w = start
    result = w
    for _ in range(n):
        if w not in bigram:
            break
        print("Predicted word:", bigram[w])
        w = bigram[w]
        result += " " + w
    return result
print("First word in data:", words[0])
print(predict(words[0]))
print("\nGenerated text:")
print(predict("intelligence", 7))
