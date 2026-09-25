#Modules - this is my module file. and I'm going to import this module and use its functions:
'''
In Python, a module is simply a file containing Python code (with a .py extension) 
that can define functions, classes, and variables.
'''

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

