# ==========================================
# Python Chatbot - Version 2
# Conversation Memory
# ==========================================
memory = {}
# ------------------------------------------
# V1: Basic chatbot responses
# ------------------------------------------

def get_response(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! 👋"

    elif "how are you" in message:
        return "I'm doing great!"

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


# ------------------------------------------
# Save information into memory
# ------------------------------------------

def save_memory(message):

    message_lower = message.lower()

    # Remember user's name
    if "my name is" in message_lower:

        name = message_lower.replace("my name is", "").strip()

        memory["name"] = name

        return f"Nice to meet you, {name}!"

    # Remember what user likes
    elif "i like" in message_lower:

        like = message_lower.replace("i like", "").strip()

        memory["likes"] = like

        return f"That's great! I'll remember that you like {like}."

    # Remember favorite color
    elif "my favorite color is" in message_lower:

        color = message_lower.replace(
            "my favorite color is", ""
        ).strip()

        memory["favorite_color"] = color

        return f"Got it! I'll remember that your favorite color is {color}."

    return None


# ------------------------------------------
# Retrieve information from memory
# ------------------------------------------

def get_memory_response(message):

    message_lower = message.lower()

    # Retrieve name
    if "what is my name" in message_lower:

        if "name" in memory:
            return f"Your name is {memory['name']}."

        else:
            return "I don't know your name yet."

    # Retrieve likes
    elif "what do i like" in message_lower:

        if "likes" in memory:
            return f"You like {memory['likes']}."

        else:
            return "I don't know what you like yet."

    # Retrieve favorite color
    elif "what is my favorite color" in message_lower:

        if "favorite_color" in memory:
            return f"Your favorite color is {memory['favorite_color']}."

        else:
            return "I don't know your favorite color yet."

    return None


# ------------------------------------------
# Chatbot starts here
# ------------------------------------------

print("=================================")
print("       🤖 Python Chatbot V2")
print("=================================")

print("I can remember some information about you.")
print("Type 'bye' to exit.\n")


while True:

    # Get user input
    message = input("You: ")


    # --------------------------------------
    # Step 1: Try to save information
    # --------------------------------------

    memory_message = save_memory(message)

    if memory_message is not None:

        print("Bot:", memory_message)


    # --------------------------------------
    # Step 2: Try to retrieve information
    # --------------------------------------

    else:

        memory_response = get_memory_response(message)

        if memory_response is not None:

            print("Bot:", memory_response)


        # ----------------------------------
        # Step 3: Normal chatbot response
        # ----------------------------------

        else:

            response = get_response(message)

            print("Bot:", response)


    # --------------------------------------
    # Exit chatbot
    # --------------------------------------

    if "bye" in message.lower():

        break