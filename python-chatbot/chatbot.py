#Python Chatbot 

print(' ========== WELCOME TO THE CHATBOT ========== ')
print("      >>>>>> 🤖 Python Chatbot <<<<<<          ")
print("=============================================")

name = input("What is your name ? ")
print(f'Nice to meet you, {name}')
print("type 'bye' to exit. \n")

while True:
    message = input("You : ")
    message = message.lower()

    if message == 'hello':
        print(f'Bot: {message}')
    elif message == 'how are you':
        print(f"Bot : I'm fine {name} !! you ??")
    elif message == 'what is your name':
        print("Bot : I'm Python chatbot 1.1v ")
    elif message =='bye':
        print(f"Good Byee !! {name}")
        break
    else:
        print("Bot: Sorry I don't understand your message")







# print("=================================")



name = input("What is your name? ")

print(f"Nice to meet you, {name}!")

message = input("You: ")

print("Bot:", message)