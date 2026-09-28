# Type Convertion

num_int = 123 #integer type
num_flo = 1.23 #float Type

num_new = num_int + num_flo
print("value of num_new : ", num_new)
print("DataType of the num_new : ", type(num_new)) #type is float becasue the right side operand is float value 


#Example 2 - simple addition 
a = 1.34
b = 59
c = a+b
print("Result : ", type(c))


#Example 3 - if a intiger and string is trying to perform, Type casting will throw the error 
#ERROR - Unsupported operand and Type(s)  for int & str

'''num_int = 123 #int
num_str = "Tester"

num_typ =  num_int + num_str
print("This will throw the ERROR : ", num_typ)'''

#Example 4
# explicitly converted to int type

num_i = 123
num_s = "456"
#now we need to convert the string explecitly into integer

num_s = int(num_s)
print(type(num_i + num_s), num_i + num_s)

#so the above value will be converted as integer since i have converted the string into integer
# 123+456 = 579


