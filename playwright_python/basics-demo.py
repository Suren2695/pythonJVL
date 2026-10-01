print("Surender loves python")
'''
str = input("What is your name ?")
print(str)
print("Test")'''

b = 100
print("{} {} {}".format("score is ", b, " for india")) #if i want to insert multiple variables or content in the print statement we need to use {}

#Demo 2

values = [1, 2, "Surender", 4, 5.7] #List
print(values[2]) # Using a index of the list and it is started from 0
print(values[-1]) #If I want the last index value
print(values[1:3]) #[2, 'Surender']
values.insert(3, "Natarajan")
print(values) #[1, 2, 'Surender', 'Natarajan', 4, 5.7]
values.append("End")
print(values)

#Demo 3 - Tuples and Dictionary please refer my Python Basics 1 - Warmup folder outside this folder 

#Demo 4 - if else looping

greet = "What is your wish ? "

if greet == "morning":
    print("condition matched")
else :
    print("end the greetings")

print("If else condition code is completed")

#Demo 5 - Dictionary 
dic = {"a":2, 4:"bcd", "c":"Hello World "}

print(dic[4])
print(dic["c"])

dict = {}
dict["firstname"] = "Suren"
dict["lastname"] = "Raj"
dict["gender"] = "Male"

print(dict)

#loops 
obj =[2,3,4,5,7,8]
for i in obj:
    print(i*2)