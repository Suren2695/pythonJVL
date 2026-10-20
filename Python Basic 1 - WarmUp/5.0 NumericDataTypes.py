# Numeric Data Types in Python
# This file demonstrates the main numeric data types: int, float, and complex.

# Integer data type
age = 25
print("Integer Example:")
print("age =", age)
print("Type of age:", type(age))

# Float data type
price = 99.99
print("\nFloat Example:")
print("price =", price)
print("Type of price:", type(price))

# Complex data type
complex_number = 3 + 4j
print("\nComplex Example:")
print("complex_number =", complex_number)
print("Type of complex_number:", type(complex_number))

# Arithmetic operations
print("\nArithmetic Operations:")
print("age + 5 =", age + 5)
print("price * 2 =", price * 2)
print("complex_number.real =", complex_number.real)
print("complex_number.imag =", complex_number.imag)

# Type conversion examples
print("\nType Conversion:")
print("float(age) =", float(age))

#Complex 
#complex number has two things ( real and imaginary ) 
#Example : 5+3j - 5 is the real number and 3 is imaginary here

c = 5+3j
print(type(c)) #<class complex>
print(c.real) #5.0
print(c.imag) #3.0
print(c) #5+3j