def get_response(message):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return message
    elif "how are you" in message:
        return "I'm fine"
    elif "what is your age" in message:
        return "I'm chatbot 1.1 v"
    elif "bye" in message:
        return "Good byee"
    else:
        return "Sorry I dont understand"

print('==========WELCOME TO CHAT BOT++++++++')   
name = input('What is your name ?')

print(f'Nice to meet you {name}')
print('enter bye to exit \n') 

while True:
    message = input("You : ")
    response = get_response(message)
    print("Bot : ", response)
    if "bye" in message:
        break
