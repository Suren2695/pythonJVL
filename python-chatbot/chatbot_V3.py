import json
from pathlib import Path
#Import Json 
#=========================
# Python Chat Bot - version 3
# Persistent memory 
#=========================

memory = {}
#MEMORY_FILE = Path(__file__).with_name("memory.json")

#-----------
#Load Memory
#-----------
def save_memory_to_file():
    with open("memory.json","w") as file:
        json.dump(memory,file,indent=4)

memory["name"] = "Surender"
save_memory_to_file()
print("Memory saved successfully")

def load_memory():
    with open("memory.json","r") as file:
        memory = json.load(file)
    return memory

#Load exisiting memory
memory = load_memory()

print("loaded memory:", memory)
print("My name is:", memory["name"])