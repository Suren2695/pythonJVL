'''
In Python, a lambda function is used to create small, anonymous, and temporary functions 
right at the spot where they are needed. Unlike a standard function defined with the def keyword, 
a lambda function is written in a single line of code, doesn't require a name, 
and automatically returns the result of its expression.
'''

#Example 1
#LAMBDA Function - basic

sqr = lambda x: x**2
print(sqr(5))

#lambda parameter: expression
#** = exponent / power

#Example 2 - cube root
sqr1 =  lambda x: x**3
print(sqr1(2))

#Example 3 - Check whether the number is positive or not 
positive = lambda x: x>0
print(positive(10)) #true
print(positive(-1)) #false

#Example 4 - Lambda with 2 inputs
input =  lambda x,y : x + y
print(input(3,2))

#Example 5 - Fins the bigger number
max = lambda x,y : x if x>y else y 
print(max(10,34)) //34
