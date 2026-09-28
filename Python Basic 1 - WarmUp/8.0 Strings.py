#String in python
#All of the following are equivalent

my_string = 'Hello'
print(my_string)

my_str = """Test"""
my_secStr = '''Suren'''
#Concat between the string
print(my_str + my_secStr )

#If i want to repeat a word multiple times 
print('repeate a word :',( my_secStr +' ' )* 3) #Suren Suren Suren 

str = 'JVL'
print('first word is ', str[0])

print('last word ', str[-1])

#Slicing 2nd Index to 5th   char
str1 = 'jvlcode'
#If a word is need to split - We have to fix the 1st index and where it need to end next word to be give.
print('str1 :',str1[0:3]) #jvl
print('str1 :', str1[3:7]) # code
print(str1[3:]) # code
print('str1:', str1[3:-1]) #cod
