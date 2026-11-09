# 🤖 Python Chatbot – V3 & V3.1
### Persistent Memory & Advanced Memory Management using Python

## 📌 Project Overview

This project is a beginner-friendly Python chatbot that gradually evolves from a basic rule-based chatbot into an application capable of storing, retrieving, updating and deleting user information.

The main objective is to strengthen Python programming fundamentals through hands-on development.

This repository currently includes:

- **V3:** Persistent Memory using JSON.
- **V3.1:** Advanced Memory Management.

## 🚀 Version 3 – Persistent Memory using JSON

### Overview

In previous versions, the chatbot could remember information only while the program was running.

In V3, JSON-based file handling was introduced to make memory persistent.

The chatbot can now save user information in a `memory.json` file and retrieve it even after restarting the application.

### Features

- Save user name.
- Save user interests and preferences.
- Store information in a JSON file.
- Load previously saved information when the application starts.
- Retrieve stored information through chatbot queries.
- Handle missing or invalid JSON files.

### Python Concepts Used

- `import json`
- `json.dump()`
- `json.load()`
- File handling using `open()`
- Read (`r`) and write (`w`) modes.
- Python dictionaries.
- Functions and conditional statements.
- Exception handling using `try` and `except`.

### Code Example – Saving Memory

```python
def save_memory_to_file():
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)
```

### Code Example – Loading Memory

```python
def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}
```

### Sample JSON Output

```json
{
    "name": "Surender",
    "like": "Python",
    "favorite": "blue"
}
```

### Sample Conversation

```text
You: My name is Surender
Bot: Nice to meet you, Surender!

You: I like Python
Bot: That's great! I'll remember that you like Python.

You: What is my name?
Bot: Your name is Surender.
```

**Key Achievement:** The chatbot can retain information even after closing and restarting the application.

---

## 🚀 Version 3.1 – Advanced Memory Management

### Overview

V3.1 builds on the persistent memory functionality introduced in V3.

The chatbot can now manage existing information by saving, updating, retrieving and deleting individual memory entries.

### Features

- Save new user information.
- Update existing information.
- Retrieve specific information.
- Display all stored information.
- Forget specific information.
- Clear all saved memory.
- Automatically update the JSON file after memory changes.

### Python Concepts Used

- Dictionary operations.
- `memory.items()`
- `del` keyword.
- `memory.clear()`
- String manipulation.
- Functions and loops.
- JSON file handling.

### Code Example – Update Memory

```python
memory["name"] = "Arun"
save_memory_to_file()
```

### Code Example – Delete Specific Memory

```python
del memory["name"]
save_memory_to_file()
```

### Code Example – Clear All Memory

```python
memory.clear()
save_memory_to_file()
```

### Sample Conversation

```text
You: My name is Surender
Bot: I have saved your name as Surender.

You: My name is Arun
Bot: I have saved your name as Arun.

You: What is my name?
Bot: Your name is Arun.

You: What do you remember about me?
Bot: Here is what I remember:
name: Arun
like: Python

You: Forget my name
Bot: I have forgotten your name.

You: Forget everything
Bot: I have forgotten all your saved information.
```

**Key Achievement:** The chatbot can now manage persistent information rather than simply storing it.

---

## 📂 Project Structure

```text
Python-Chatbot/
│
├── V1/
│   └── chatbot.py
│
├── V2/
│   └── chatbot.py
│
├── V3/
│   ├── chatbot.py
│   └── memory.json
│
├── V3.1/
│   ├── chatbot.py
│   └── memory.json
│
└── README.md
```

## ⚙️ Installation & Execution

### Prerequisites

- Python 3.x
- Visual Studio Code or any Python-supported IDE.
- Basic knowledge of Python.

### Step 1 – Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2 – Navigate to the project folder

```bash
cd Python-Chatbot
```

### Step 3 – Run V3

```bash
python V3/chatbot.py
```

### Step 4 – Run V3.1

```bash
python V3.1/chatbot.py
```

**Note:** Each version uses its own `memory.json` file. Start with an empty JSON dictionary `{}` if you want a fresh memory.

---

## 📚 Learning Journey

| Version | Implementation | Status |
|---|---|---|
| V1 | Basic Rule-Based Chatbot | Completed |
| V2 | Conversational Memory | Completed |
| V3 | Persistent Memory using JSON | Completed |
| V3.1 | Advanced Memory Management | Completed |
| V4 | LLM Integration | Planned |
| V5 | Retrieval-Augmented Generation (RAG) | Planned |
| V6 | Agentic AI | Planned |

## 🔮 Future Enhancements

The next versions will focus on transforming this basic chatbot into an AI-powered application.

- Integrate an LLM through an API.
- Implement intelligent conversational responses.
- Introduce Retrieval-Augmented Generation (RAG).
- Integrate embeddings and vector databases.
- Enable document-based question answering.
- Explore Agentic AI and tool calling.
- Build a simple user interface.

## 🎯 Key Takeaways

This project helped me gain practical experience with:

- Python programming fundamentals.
- File handling and JSON operations.
- Persistent data storage.
- Dictionary and list manipulation.
- Exception handling.
- Building and improving an application incrementally.

## 👨‍💻 Author

**Surender**

Building my Python skills through practical projects and continuous learning.

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback!

**Learning by building. Improving one version at a time. 🚀**