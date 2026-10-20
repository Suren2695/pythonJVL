'''
The range() function returns a sequence of numbers, 
starting from 0 by default, and increments by 1 (by default), 
and stops before a specified number.
'''
#We can create lists, tuples, sets, dictionary

number = range(1,6)

print(list(number))
print(tuple(number))
print(set(number))
print(dict.fromkeys(number,99)) #DICTIONARY CREATION IN THE KEY AND VALUES PAIR
#{1: 99, 2: 99, 3: 99, 4: 99, 5: 99}

#step in range
numbers = range(1,6,2)
print(list(numbers)) #[1, 3, 5]

numbers3 = range(5,0,-1)
print(list(numbers3))