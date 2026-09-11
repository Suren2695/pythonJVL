#list

'''
   - An ordered collection of items enclosed in square brackets [ ].
   - Mutable, allowing you to modify, add, or remove elements.
   - Example: `my_list = [1, 2, 3, 4, 5]`
'''

#empty list 
my_list = []

#list of integers
my_lis = [1,2,3,4]

#list with mixed data types
my_list1 = [1, "hello", 3.14]

#Example1
language = ["French", "German","English","Czech"]

#Accessing first element
print(language[0]) #French ( Indexing - first)

#Accessing the 4 element
print(language[3])

#Changing the 4th value on the list 

language[3] = "tamil"
print(language)

#Example 2
numbers = [10, 20, 30, 40, 50]
print(numbers[0]) #10
print(numbers[-1]) #50

#Example 3
#Add an Element in the list
numbers.append(60)
print(numbers)

#Example 4
#Insert an Element
#Insert 25 in the index 2

numbers.insert(2,25)
print(numbers)

#Example 5
#Remove the element
numbers.remove(30)
print(numbers)

#Example 6
#length of the list
print(len(numbers))

#Eample 7
#maximum value inthe aRRAY

print(max(numbers))

#Example 8
#Reverse the number
print(reversed(numbers))

#Example 9
#Sort a list 
numbers = [50, 10, 30, 20, 40, 2, 4, 2, 6,99, 2, 0, 3, 1, 3, 5, 4]
numbers.sort()
print(numbers)

#Example 10
# Count Occurrences - Count how many times 2 appears in the list.
occ = numbers.count(2)
print(occ)

#Example 11
#Remove duplicate values from a list.

uniq_num = list(set(numbers))
print(uniq_num)
print(set(numbers))

#Example 12
#Find even numbers
numb = [1, 2, 3, 4, 5, 6]
evens = [num for num in numb if num % 2 == 0]
print(evens)