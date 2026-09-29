# Here My Goal is to learn python Basics to Inter level

So starting of from 
# BASICS 1 - Warmup Folder 
References :
 1. JVL Code ( Tamil ) - https://www.jvlcode.com/
 2. AI Coach John - https://www.youtube.com/watch?v=QGAuolgCTHE&t=

## JVL Code 
1. Basics 1 - Warmup Folder 
- First Python program, Intendation in python
- Print Function, Variable, Operators, Getting Input, Comments
- Type Convertion/casting, Numeric Data Types
- List, Tuples, String, Sets, Dictionary, Range
- If Else Statment,While, For, Break Statement, Continue
- Functions, lambda Function, Modules
- Open Files, Write, Read, Expection handeling, Dictionary operations,
- Class, objects, Constractor, Inheritance.

# Mutability:
  - Strings, tuples: Immutable (cannot be changed after creation).
  - Lists, dictionaries, sets: Mutable (can be modified).

# Order:
  - Strings, lists, tuples: Ordered (elements have a specific order).
  - Dictionaries, sets: Unordered (no specific order of elements).

# Access:
  - Lists, tuples, strings: Elements can be accessed by index.
  - Dictionaries: Elements are accessed by keys.
  - Sets: Elements are not accessed by index; they are used for membership testing and set operations.

# Syntax:
  - Strings: Enclosed in quotes.
  - Lists: Enclosed in [ ].
  - Tuples: Enclosed in ( ) or without enclosing symbols.
  - Dictionaries: Enclosed in { } with key-value pairs.
  - Sets: Enclosed in { } with unique elements.

### smartdesk-ai-chatbot ###
# Project idea #

"SmartDesk AI – A Python-based AI Assistant Chatbot"

A chatbot that can:

💬 Chat with the user
🧠 Remember conversation context
📚 Answer questions from a small knowledge base
🔍 Search/retrieve information from your own documents
🧮 Perform simple calculations
🐍 Demonstrate Python concepts
📝 Maintain conversation history
🌐 Expose an API using FastAPI
🖥️ Have a simple UI using Streamlit
🤖 Later integrate an LLM/API

This gives you a project that starts very simple but can evolve into an impressive AI/GenAI project.

# PHASE 1 #
I have done the terminal based chatbot which is very simple.

### Python Playwright Automation ###

# What is a virtual environment?

A virtual environment (venv) is a separate Python environment created specifically for one project.
PythonJVL/
│
├── Python_Basics_1/
│   ├── .venv/
│   ├── functions.py
│   └── loops.py
│
├── Python_Chatbot/
│   ├── .venv/
│   ├── chatbot.py
│   └── README.md
│
└── Playwright_Python/
    ├── .venv/
    ├── tests/
    ├── pages/
    ├── config.py
    └── conftest.py

Each project can have its own packages and package versions.
Mainly to avoid the conflicts.

# When you create:
python -m venv .venv

PYTHON Creates:
your-project/
│
└── .venv/
    ├── Scripts/
    ├── Lib/
    └── ...

Now this project has its own package environment.

When you activate it:
.venv\Scripts\Activate.ps1

your terminal changes to something like:
(.venv) PS C:\Users\Surender\playwright-project>

That (.venv) tells you:
I'm currently working inside this project's Python environment.