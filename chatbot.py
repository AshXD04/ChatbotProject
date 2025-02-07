import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm good, thanks for asking!", "I'm doing well, how about you?"]
    ],
    [
        r"(.*) your name?",
        ["I'm a chatbot created in Python!", "You can call me ChatBot!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure! How can I assist you?", "What do you need help with?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "Interesting... Tell me more!"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
