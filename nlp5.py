from langdetect import detect
from googletrans import Translator
text = "எனக்கு சாப்பாடு வேண்டும்"
print("Detected Language:", detect(text))
translator = Translator()
print("Translated Text:", translator.translate(text, dest='en').text)
