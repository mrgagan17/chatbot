import nltk
import random
import string  # To process standard Python strings
from nltk.chat.util import Chat, reflections

# Define chatbot responses using predefined patterns
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks!", "I'm just a bot, but I'm good!", "I'm great! What about you?"]
    ],
    [
        r"what is your name ?|your name?",
        ["I'm a Zomboie!", "I don't have a name, but you can call me Zombie!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Take care!"]
    ],
    [
        r"(.*) your name ?",
        ["I am just a simple chatbot.", "You can call me ChatBot."]
    ],
    [
        r"(.*) help (.*)",
        ["I'm here to assist you. What do you need help with?", "How can I assist you?"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", "Could you rephrase your question?", "Interesting... Tell me more!"]
    ]
]

# Create chatbot using Chat class
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
start_chat()