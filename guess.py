import random

secret_num = random.randint(1, 30)

input_= input("Guess a number: ")

user_input = int(input_)

if user_input < secret_num: 
    print("Your guess is too low to the secret number: " + str(secret_num) )
elif user_input > secret_num: 
    print("Your guess is too high to the secret number: " + str(secret_num) )
else:
    print(user_input + " is a right guess")