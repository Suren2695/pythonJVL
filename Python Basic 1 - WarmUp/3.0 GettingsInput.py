#Input string - The prompt string, 
#if given, is printed to standard output without a trailing newline before reading input.

inputString = input("Enter the string : ")
print("The entered string is = ", inputString)

# Voting eligibility 
# Take age as input and print whether the person can vote.

age = int(input("Your age is : "))
if age > 18:
    print(age,"So your eligible")
else:
    print("Kiddo")

### Number guessing game Store a secret number, 
# ask the user to guess it, and tell them whether the guess is too high, too low, or correct.

secret_number = 9

while True:
    guess_number = int(input("Guess Number is : "))

    if guess_number < secret_number:
        print("The input value is low")
    elif guess_number > secret_number:
        print("The input value is high")
    else:
        print("Correct guess!")
        break
