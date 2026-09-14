'''
A Python dictionary is a built-in data structure used to store data in key-value pairs. 
It is highly efficient for data retrieval because it functions like a hash table, mapping unique keys to specific values.
'''
#Empty Dictionary
my_dict = {}

#dictionary with integer key
my_dic = {1:"Surender",2:"natarajan"}
print(my_dic)

#not only integer key,But we can give any kind of datatypes as key
a = {"Name":"Surender", 1:[2,4,3]}
print(a) #{'Name': 'Surender', 1: [2, 4, 3]}

#Example
person = {'name':"jackson", 'age':26}
print(person['age']) #26

#change the age to 31
person["age"] = 31
print(person) #{'name': 'jackson', 'age': 31}

#Adding a salary key and value pair
person["salary"] = 100000
print(person) #{'name': 'jackson', 'age': 31, 'salary': 100000}

#Deletion
del person["salary"]
print(person) #{'name': 'jackson', 'age': 31}

#Delete the entire dictionary
#del person -  this will delete the dictionary 
