#Looping in Python is a programming feature that allows you to execute a specific block of code repeatedly. 
#Instead of writing the exact same lines of code over and over again, a loop automates the repetitive task until a certain condition is met

#IF .... ELSE Statement

num =-1
if num > 0:
    print("positive number")
elif num == 0:
    print("Zero")
else:
    print("negative") #negative

#WHILE loop
n = 100
#initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum +i
    i = i+1
    print('value is :', sum)

