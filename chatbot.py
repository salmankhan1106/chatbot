import nltk
from nltk.chat.util import Chat , reflections
from datetime import datetime
nltk.download("punkt")

pairs = [
    [
        r"hi|hello|hey",
        ["hello",
         "Hi There",
         "Hey !"]
    ],
    [
        r"how are you",
        ["I'm good thankyou. What about you !"
         , "I'm doing well , Thankyou"]
    ],
    [
        r"what is your name",
        ["I'm chatbot created by you. You can call me chatbot!"]
    ],
    [
        r"quit",
        ["Bye, Take care!",
        "It was nice talking to you. Goodbye!"]
    ],
    [
        r"what time is it ?|can you tell me the time ?|what is the time ?|time",
        ["The current time is " + datetime.now().strftime("%H:%M:%S"), 
        "It's " + datetime.now().strftime("%H:%M:%S")]
    ],
    [
        r"what is the date today ?|can you tell me the date ?|what's the date ?|date",
        ["Today's date is " + datetime.now().strftime("%d-%m-%Y"),
        "It's " + datetime.now().strftime("%d-%m-%Y")]
    ]       
]
chatbot = Chat(pairs,reflections)

def chatbot_conversation():
    
    print(" ")
    print("Hi I'm chatbot. Type 'quit' to exit!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower()=="quit":
            print("ChatBot: GoodBye!")
            break;
        response = chatbot.respond(user_input)
        print("ChatBot: ",response) 
chatbot_conversation()        