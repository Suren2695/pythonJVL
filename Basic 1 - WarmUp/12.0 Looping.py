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


#FOR loop

    numb = [2,3,6,4,7,8]
    sum = 0
    for val in numb:
        sum = sum + val
        print('The sum is : ',sum )

#BREAK

for val in "String":
    if val == 'r':
        break
    print(val) #s,t
print("The end ...")   

#Continue :
for val in "string":
    if val == 'r':
        continue
    print(val) #s,t,i,n,g
print('The end')