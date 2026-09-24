#Python chatbot

def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return message
    elif "how are you" in message:
        return "I'm fine"
    elif "what is your age" in message:
        return "I am bot 1.1V."

    elif "your name" in message:
        return "I'm PythonBot."

    elif "python" in message:
        return "Python is a high-level programming language."

    elif "thank" in message:
        return "You're welcome!"

    elif "bye" in message:
        return "Goodbye! 👋"
    else:
        return "Sorry, I don't understand that yet."

print("=================================")
print("       🤖 Python Chatbot")
print("=================================")

name = input("What is your name? ")

print(f"Nice to meet you, {name}!")
print("Type 'bye' to exit.\n")


while True:
    message = input("You: ")
    response = get_response(message)
    print("Bot:", response)
    if "bye" in message.lower():
        break