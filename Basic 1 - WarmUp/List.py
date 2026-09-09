#list

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