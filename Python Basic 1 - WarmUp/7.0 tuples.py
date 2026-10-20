#Tuples - only difference in tuples and list is, In tuples we cannot change the values in the tuples.
'''
- Similar to a list but enclosed in parentheses ( ) or without any enclosing symbols.
   - Immutable, so its elements cannot be changed after creation.
   - Example: `my_tuple = (1, 2, 3)`
'''
language = ("French", "polish", "Czech", "German")


print(language)
print(language[-1])
print(language[3])

# del language  -----#delete the entire laguage variable 

#find the length of the tuples

number = (10, 50, 20, 30, 80, 100, 90, 72 , 20, 50, 60, 20)
print(len(number)) 

#Count the occurances - how many times 20 appeared
print(number.count(20))

#Index of the element
print(number.index(20))

#Fidn the index of the element of 20 from the reverse order 
print(len(number)-1-number[::-1].index(20))
#12-1-0 = 11, So index of 11 is 20 which is from the last
#first reversing the tuple and then minusing that with length -1
