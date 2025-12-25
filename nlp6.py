import re, pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

chat = [
    "12/31/20, 23:59 - Alice: Happy new year",
    "01/01/21, 00:01 - Bob: Thank you",
    "01/01/21, 00:05 - Alice: Did you see the fireworks",
    "01/02/21, 08:10 - Charlie: Good morning everyone",
    "01/02/21, 08:12 - Bob: Morning",
    "01/02/21, 08:15 - Alice: Lets catch up later",
    "01/03/21, 10:00 - Charlie: Sure sounds good"
]

pat = r"\d+/\d+/\d+, \d+:\d+ - (.*?): (.*)"
data = [re.match(pat, c).groups() for c in chat]

df = pd.DataFrame(data, columns=["author", "message"])

# Messages per user
df.author.value_counts().plot(kind="bar", title="Messages per User")
plt.show()

# WordCloud
WordCloud(background_color="white").generate(" ".join(df.message)).to_image().show()

# Sentiment
df["label"] = df.message.apply(
    lambda x: "Positive" if TextBlob(x).sentiment.polarity > 0
    else "Negative" if TextBlob(x).sentiment.polarity < 0
    else "Neutral"
)

print(df)
df.label.value_counts().plot(kind="bar", title="Sentiment Distribution")
plt.show()
