# Creating a chatbot with conversational memory
#=================================================
#   Python Chatbot -  version 2
#   Conversational Memory
#=================================================

memory = {}

#getting response

def get_response(message):
    if "Hello" in message or "hi" in message:
        return message
    elif "How are you" in message:
        return "I'm doing great !"
    elif "your name" in message:
        return "I'm PythonBot "
    elif "Python" in message:
        return "Python is a high-level programming language."
    elif "thank" in message:
        return "You're Welcome !!"
    elif "bye" in message:
        return "Good Bye !!"
    else:
        return "Sorry I'dont understand that"

#Save memeory 
def save_memory(message):
    message_lower = message.lower()

    if "my name is" in message_lower:
        name = message_lower.replace("my name is","").strip()
        memory["name"] = name
        return f"Nice to meet you, {name}!"
    elif "i like" in message_lower:
        like = message_lower.replace("i like", "").strip()
        memory["like"] = like
        return f"That's great! I'll remember that you like {like}"
    elif "my favorite colour is" in message_lower:
        favorite = message_lower.replace("my favorite colour is", "").strip()
        memory["favorite"] = favorite
        return f"That's great, i remember your favorite colour is {favorite}"