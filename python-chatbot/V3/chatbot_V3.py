import json

# ==========================================
# PYTHON CHATBOT - VERSION 3
# Persistent Memory using JSON
# ==========================================

MEMORY_FILE = "memory.json"

# ------------------------------------------
# 1. LOAD MEMORY FROM JSON FILE
# ------------------------------------------

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# ------------------------------------------
# 2. SAVE MEMORY INTO JSON FILE
# ------------------------------------------

def save_memory_to_file():
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


# ------------------------------------------
# 3. INITIALIZE MEMORY
# ------------------------------------------

memory = load_memory()


# ------------------------------------------
# 4. SAVE USER INFORMATION
# ------------------------------------------

def save_memory(message):

    message_lower = message.lower()

    if "my name is" in message_lower:

        name = message_lower.replace("my name is", "", 1).strip()

        if not name:
            return "Please tell me your name."

        memory["name"] = name
        save_memory_to_file()

        return f"Nice to meet you, {name}!"

    elif message_lower.startswith("i like"):

        like = message_lower.replace("i like", "", 1).strip()

        if not like:
            return "What do you like?"

        memory["like"] = like
        save_memory_to_file()

        return f"That's great! I'll remember that you like {like}."

    elif "my favorite colour is" in message_lower or "my favorite color is" in message_lower:

        favorite = message_lower.replace("my favorite colour is", "", 1)
        favorite = favorite.replace("my favorite color is", "", 1).strip()

        if not favorite:
            return "Please tell me your favorite colour."

        memory["favorite"] = favorite
        save_memory_to_file()

        return f"I'll remember your favorite colour is {favorite}."

    return None


# ------------------------------------------
# 5. RETRIEVE INFORMATION FROM MEMORY
# ------------------------------------------

def get_memory_response(message):

    message_lower = message.lower()

    if "what is my name" in message_lower:

        if "name" in memory:
            return f"Your name is {memory['name']}."

        return "I don't know your name yet."

    elif "what do i like" in message_lower:

        if "like" in memory:
            return f"You like {memory['like']}."

        return "I don't know what you like yet."

    elif "what is my favorite colour" in message_lower or "what is my favorite color" in message_lower:

        if "favorite" in memory:
            return f"Your favorite colour is {memory['favorite']}."

        return "I don't know your favorite colour yet."

    return None


# ------------------------------------------
# 6. NORMAL CHATBOT RESPONSES
# ------------------------------------------

def get_response(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "how are you" in message:
        return "I'm doing great! How about you?"

    elif "what is your name" in message or "your name" in message:
        return "I'm PythonBot V3."

    elif "python" in message:
        return "Python is a high-level programming language."

    elif "thank" in message:
        return "You're welcome!"

    elif "bye" in message:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that."


# ------------------------------------------
# 7. MAIN CHATBOT EXECUTION
# ------------------------------------------

print("===================================")
print("       Welcome to PythonBot V3")
print("===================================")

print("I can remember your name, likes and favorite colour.")
print("Type 'bye' to exit.\n")


while True:

    message = input("You: ").strip()

    # Handle empty input
    if not message:
        print("Bot: Please enter something.")
        continue

    # First: Check whether user is sharing information
    response = save_memory(message)

    # Second: Check previously saved information
    if response is None:
        response = get_memory_response(message)

    # Third: Provide normal chatbot response
    if response is None:
        response = get_response(message)

    print("Bot:", response)

    # Exit chatbot
    if message.lower() == "bye":
        break
