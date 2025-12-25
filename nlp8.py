import nltk
print(" Welcome to the College Enquiry Chatbot! Type 'bye' to exit.")
college_bot = {
    "hello": "Hello!I am your college Enquiry chatbot. How can I help you today?",
    "hi": "Hi!I am your college Enquiry chatbot. How can I help you today?",
    "course": "We offer various courses in engineering, arts, and science.",
    "admission": "Admissions start in June.",
    "fees": "The fee structure varies by course.",
    "placement": "Our college has good placement records.",
    "contact": "You can contact us at 9876543210"
}
while True:
    q = input("You: ").lower()
    if q == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    for k in college_bot:
        if k in q:
            print("Bot:", college_bot[k])
            break
    else:
        print("Bot: Please ask a valid college enquiry.")
