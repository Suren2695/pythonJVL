#FUNCTIONS

#1. Basic functions
def prin_line():
    print("The line is cool") 
prin_line()
#It is mandatory to call the function outside

#Example 2 - sum of 2 numbers

def add_numbers(a,b):
    sum = a+b
    print(sum)
add_numbers(3,2)

#Example 3 - Return the sum 

def return_sum(a,b):
    return a+b
result = return_sum(3,5)
print(result)

#assign value - a,b to a variable.

def test(a,b):
    sum = a+b
    return sum
print(test(8,9))

#Rrecurssive function
#factorial of a number
def rec_fun(x):
    if x==1:
        return 1
    else:
        return(x*rec_fun(x-1))

num = 6
print("The factorial number of ", num , 'is', rec_fun(num))

#What are *args ?
#Allows a function to accept multiple positional arguments

def add(*args):
    return sum(args)
print(add(10, 20, 30))
#output is 60 


#What is **kwargs ?
#Allows multiple keyword arguments

def usr_details(**kwargs):
    print(kwargs) 
usr_details(name = 'John', age = 31)

