# 🤖 Python Chatbot — Version 1

A simple rule-based chatbot built using Python.

This is the first version of my Python chatbot learning project. The goal of this project is to understand the fundamentals of Python programming by building a small, working chatbot from scratch.

---

## 📌 Project Overview

This chatbot runs in the terminal and can:

* Greet the user
* Respond to simple questions
* Identify common keywords
* Provide predefined responses
* Continue the conversation using a `while` loop
* Exit the conversation when the user says `bye`

### Example

```text
=================================
       🤖 Python Chatbot
=================================

You: hello
Bot: Hello! 👋

You: how are you?
Bot: I'm doing great!

You: what is Python?
Bot: Python is a high-level programming language.

You: bye
Bot: Goodbye! 👋
```

---

# 🛠️ Technologies Used

* Python 3
* VS Code
* Terminal / Command Prompt

No external libraries are required for Version 1.

---

# 📂 Project Structure

```text
python-chatbot/
│
├── chatbot.py
│
└── README.md
```

---

# 🧑‍💻 Python Concepts Used

This project was created to practice the following Python concepts:

### 1. Variables

```python
message = input("You: ")
```

A variable is used to store the user's message.

---

### 2. `input()`

```python
message = input("You: ")
```

`input()` allows the program to receive information from the user.

---

### 3. Functions

```python
def get_response(message):
```

The function is responsible for processing the user's message and returning an appropriate response.

---

### 4. `if`, `elif`, and `else`

```python
if "hello" in message:
    return "Hello! 👋"

elif "python" in message:
    return "Python is a programming language."

else:
    return "Sorry, I don't understand that yet."
```

These conditions allow the chatbot to determine which response to provide.

---

### 5. String Methods

```python
message.lower()
```

Converts the user's message to lowercase so that the chatbot can handle different combinations of uppercase and lowercase letters.

For example:

```text
HELLO
Hello
hello
HeLLo
```

All can be converted to:

```text
hello
```

---

### 6. `while` Loop

```python
while True:
```

The `while` loop allows the chatbot to continue accepting messages instead of stopping after one interaction.

---

### 7. `break`

```python
if "bye" in message.lower():
    break
```

`break` stops the `while` loop and ends the chatbot conversation.

---

# 🧠 How the Chatbot Works

The basic flow is:

```text
                Start
                  │
                  ▼
          Get user message
                  │
                  ▼
          Convert to lowercase
                  │
                  ▼
          Send message to
          get_response()
                  │
                  ▼
          Find matching keyword
                  │
         ┌────────┼────────┐
         ▼        ▼        ▼
      Greeting  Python   Unknown
         │        │        │
         ▼        ▼        ▼
      Response  Response  Default
         │        │        │
         └────────┼────────┘
                  ▼
            Print response
                  │
                  ▼
           Did user say bye?
              /       \
            Yes        No
             │          │
             ▼          │
            Stop ◄──────┘
```

---

# 💻 Source Code

Create a file called:

```text
chatbot.py
```

Add the following code:

```python
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


print("=================================")
print("       🤖 Python Chatbot")
print("=================================")

print("Type 'bye' to exit.\n")


while True:

    message = input("You: ")

    response = get_response(message)

    print("Bot:", response)

    if "bye" in message.lower():
        break
```

---

# ▶️ How to Run

## Step 1 — Check Python

Open your terminal and run:

```bash
python --version
```

Example:

```text
Python 3.12.5
```

---

## Step 2 — Clone the Repository

If the project is already available on GitHub:

```bash
git clone <your-repository-url>
```

Then move into the project:

```bash
cd python-chatbot
```

---

## Step 3 — Run the Chatbot

Run:

```bash
python chatbot.py
```

You should see:

```text
=================================
       🤖 Python Chatbot
=================================

Type 'bye' to exit.
```

Start chatting.

---

# 🧪 Example Conversation

```text
You: hello
Bot: Hello! 👋

You: what is your name
Bot: I'm PythonBot.

You: what is python
Bot: Python is a high-level programming language.

You: how are you
Bot: I'm doing great!

You: thank you
Bot: You're welcome!

You: bye
Bot: Goodbye! 👋
```

---

# 📚 What I Learned

While building Version 1, I practiced:

* Python variables
* User input
* Functions
* Function parameters
* Return values
* `if / elif / else`
* `while` loops
* `break`
* String methods
* Keyword matching
* Basic program structure

---

# 🚧 Current Limitations

This is a **rule-based chatbot**, so it does not use Artificial Intelligence or an LLM.

For example:

```text
You: Tell me something interesting about Python
Bot: Sorry, I don't understand that yet.
```

The chatbot only understands messages for which predefined rules exist.

---

# 🚀 Future Improvements

This project will be developed incrementally.

### Version 2 — Conversation Memory

Add the ability to remember information during a conversation.

Example:

```text
You: My name is Surender
Bot: Nice to meet you, Surender!

You: What is my name?
Bot: Your name is Surender.
```

### Version 3 — Persistent Memory

Store conversation information using:

* JSON
* SQLite
* Database

### Version 4 — AI Integration

Connect the chatbot to an LLM/API so that it can generate dynamic responses instead of relying only on predefined rules.

### Version 5 — RAG

Add a knowledge base so the chatbot can answer questions based on documents.

```text
Documents
    ↓
Knowledge Base
    ↓
Search / Retrieval
    ↓
Relevant Information
    ↓
AI Response
```

### Version 6 — Web Interface

Build a user interface using Streamlit.

### Version 7 — API

Create a backend API using FastAPI.

### Version 8 — Testing & CI/CD

Add:

* PyTest
* API testing
* Automated tests
* GitHub Actions

---

# 🎯 Project Goal

The long-term goal of this project is to evolve a simple Python chatbot into a small **AI-powered conversational application** while learning Python, APIs, LLMs, RAG, testing, and application architecture step by step.

---

## 📈 Project Evolution

```text
Version 1
Rule-Based Chatbot
       ↓
Version 2
Conversation Memory
       ↓
Version 3
Persistent Memory
       ↓
Version 4
LLM Integration
       ↓
Version 5
RAG / Knowledge Base
       ↓
Version 6
Streamlit UI
       ↓
Version 7
FastAPI Backend
       ↓
Version 8
Testing + CI/CD
       ↓
Final AI Chatbot
```

---

## 👨‍💻 Author

**Surender**

This project is part of my hands-on journey to learn Python and build practical AI/GenAI applications.
