import nltk

print("Welcome to the Tourist Guide Chatbot!")
print("Type 'bye' to exit.\n")

tourist_bot = {
    "hello": "Hello! I am your AI-based tourist guide. How can I help you?",
    "hi": "Hi! I am your AI-based tourist guide. How can I help you?",
    "places": "You can visit beaches, hill stations, historical monuments, and wildlife sanctuaries.",
    "beach": "Popular beaches include Goa, Kovalam, and Marina Beach.",
    "hill station": "Popular hill stations include Ooty, Manali, and Munnar.",
    "monument": "Famous monuments include Taj Mahal, Red Fort, and Qutub Minar.",
    "food": "You can enjoy local cuisines like dosa, biryani, and seafood.",
    "best time": "The best time to travel is from October to March.",
    "transport": "You can travel by bus, train, or flight depending on your location.",
    "hotel": "You can find hotels ranging from budget to luxury.",
    "contact": "For tourism help, contact the local tourism office."
}

while True:
    q = input("You: ").lower()

    if q == "bye":
        print("Bot: Goodbye! Have a safe and happy journey 😊")
        break

    for key in tourist_bot:
        if key in q:
            print("Bot:", tourist_bot[key])
            break
    else:
        print("Bot: Sorry, I don't have information on that. Please ask about tourist places, food, or travel.")
