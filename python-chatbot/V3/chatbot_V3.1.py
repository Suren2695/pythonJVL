
import json

# ==========================================
# PYTHON CHATBOT - VERSION 3.1
# Advanced Memory Management
# ==========================================

MEMORY_FILE = "memory.json"


# ------------------------------------------
# 1. LOAD MEMORY
# ------------------------------------------

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# ------------------------------------------
# 2. SAVE MEMORY TO JSON
# ------------------------------------------

def save_memory_to_file():
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


# ------------------------------------------
# 3. INITIALIZE MEMORY
# ------------------------------------------

memory = load_memory()


# ------------------------------------------
# 4. SAVE OR UPDATE USER INFORMATION
# ------------------------------------------

def save_memory(message):

    message_lower = message.lower().strip()

    if message_lower.startswith("my name is"):
        name = message.strip()[len("my name is"):].strip()

        if not name:
            return "Please provide your name."

        memory["name"] = name
        save_memory_to_file()

        return f"I have saved your name as {name}."

    elif message_lower.startswith("i like"):
        like = message.strip()[len("i like"):].strip()

        if not like:
            return "Please tell me what you like."

        memory["like"] = like
        save_memory_to_file()

        return f"I have saved that you like {like}."

    elif message_lower.startswith("my favorite colour is") or message_lower.startswith("my favorite color is"):

        prefix = (
            "my favorite colour is"
            if message_lower.startswith("my favorite colour is")
            else "my favorite color is"
        )

        favorite = message.strip()[len(prefix):].strip()

        if not favorite:
            return "Please tell me your favorite colour."

        memory["favorite"] = favorite
        save_memory_to_file()

        return f"I have saved your favorite colour as {favorite}."

    return None


# ------------------------------------------
# 5. RETRIEVE SAVED INFORMATION
# ------------------------------------------

def get_memory_response(message):

    message_lower = message.lower().strip()

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

    elif "what do you remember about me" in message_lower:
        if not memory:
            return "I haven't saved anything about you yet."

        details = []

        for key, value in memory.items():
            details.append(f"{key}: {value}")

        return "Here is what I remember:\n" + "\n".join(details)

    return None


# ------------------------------------------
# 6. FORGET SPECIFIC OR ALL MEMORY
# ------------------------------------------

def forget_memory(message):

    message_lower = message.lower().strip()

    if message_lower in ["forget everything", "forget all", "clear all memory"]:
        if not memory:
            return "There is no saved information to delete."

        memory.clear()
        save_memory_to_file()

        return "I have forgotten all your saved information."

    elif message_lower in ["forget my name", "forget name"]:
        key = "name"

    elif message_lower in ["forget what i like", "forget my likes"]:
        key = "like"

    elif message_lower in [
        "forget my favorite colour",
        "forget my favorite color"
    ]:
        key = "favorite"

    else:
        return None

    if key in memory:
        del memory[key]
        save_memory_to_file()

        return f"I have forgotten your {key}."

    return f"I don't have your {key} saved."


# ------------------------------------------
# 7. NORMAL CHATBOT RESPONSES
# ------------------------------------------

def get_response(message):

    message_lower = message.lower()

    if "hello" in message_lower or "hi" in message_lower:
        return "Hello! How can I help you?"

    elif "how are you" in message_lower:
        return "I'm doing great! How about you?"

    elif "what is your name" in message_lower or "your name" in message_lower:
        return "I'm PythonBot V3.1."

    elif "python" in message_lower:
        return "Python is a high-level programming language."

    elif "thank" in message_lower:
        return "You're welcome!"

    elif message_lower == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that."


# ------------------------------------------
# 8. MAIN CHATBOT EXECUTION
# ------------------------------------------

print("===================================")
print("       Welcome to PythonBot V3.1")
print("===================================")

print("I can save, update, retrieve and forget information.")
print("Type 'bye' to exit.\n")


while True:

    message = input("You: ").strip()

    if not message:
        print("Bot: Please enter something.")
        continue

    # Exit chatbot
    if message.lower() == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    # First: Check forget commands
    response = forget_memory(message)

    # Second: Check whether user is sharing information
    if response is None:
        response = save_memory(message)

    # Third: Retrieve saved information
    if response is None:
        response = get_memory_response(message)

    # Fourth: Normal chatbot response
    if response is None:
        response = get_response(message)

    print("Bot:", response)
