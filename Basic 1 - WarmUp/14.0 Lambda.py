'''
In Python, a lambda function is used to create small, anonymous, and temporary functions 
right at the spot where they are needed. Unlike a standard function defined with the def keyword, 
a lambda function is written in a single line of code, doesn't require a name, 
and automatically returns the result of its expression.
'''

#Example 1
#LAMBDA Function - basic

sqr = lambda x: x*x

print(sqr(5))