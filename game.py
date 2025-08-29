import random

# A number guessing game

""" secret_num = random.randint(1, 30)

input_= input("Guess a number: ")

user_input = int(input_)

if user_input < secret_num: 
    print("Your guess is too low to the secret number: " + str(secret_num) )
elif user_input > secret_num: 
    print("Your guess is too high to the secret number: " + str(secret_num) )
else:
    print(user_input + " is a right guess") """

# A word scramble game
word = ["zayn", "goat", "ronaldo", "genius", "jimmy", "jane", "precious"]

computer_choice = random.choice(word)
scramble = "".join(random.sample(computer_choice, len(computer_choice)))

print("******************")
print("*                *")
print("*      "+str(scramble)+"   *")
print("*                *")
print("******************")
print("")
user_input = input("What is the right word for this scramble: ")
if user_input  == computer_choice:
    print("Yahh! you made a rigth guess")
else: 
    print("That was wrong! Try again")
