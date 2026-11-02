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

#EXAMPLE 1 - billing claculator 

price =  1200
tax = price * 0.18
print(tax)
total = price + tax

print(total)

if total > 1000:
    total_Discount = total * 0.10
    print( 'Total discount is : ', total_Discount)
    total -= total_Discount
print(total)

#Example 2:
obj = [2,3,5,7,9]
for i in obj:
    print(i)

for i in obj:
    print(i*2)

#sum of first natural number 1+2+3+4+5 = 15
suma = 0
for j in range(1,6):  #range(i,j) -> i  to j-1
    suma = suma + j
print(suma)
print("********")

#If i want to incremental by 2 for each iteration 
for j in range(1,10,2):
    print(j)
    suma = suma + j
print(suma)