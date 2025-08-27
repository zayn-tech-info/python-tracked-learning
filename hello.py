# Greeting Program

""" name = input("Enter your name and age to get a greeting: ")
age = int(input("Now enter your age: "))
print("Hey " + name + "! " + "your are " + str(age) + " years old") """

# Odd or Even Checker

""" number = int(input('Enter a number: '))
if number % 2 == 0: 
      print('The number you provide is an even number')
else:
      print('The number you provide is an odd number') """

# Simple Grade Checker

""" grade = int(input('Enter your grade: '))

if grade <= 100 and grade >= 70:
      print('Your grade is A')
elif grade <= 69 and grade >= 60:
      print('Your grade is B')
elif grade <= 56 and grade >= 50:
      print('Your grade is C')
elif grade <= 49 and grade >= 40:
      print('Your grade is D')
else: 
      print('Your grade is E') """
 
 
#  Type Conversion Test

""" typ = input('Enter just anything: ')

print(type(typ))
int_typ = int(typ)
float_typ = float(typ)
str_typ = str(typ)
print(int_typ)
print(float_typ)
print(str_typ)
print(type(int_typ))
print(type(float_typ))
print(type(str_typ)) """


# Swap Variables

""" name = "zayn"
name2 = "mariam"

name, name2 = name2, name
print(name, " name")
print(name2, " name2") """

names = ["zayn", "dave", "john"]
actions = ["codes", "eats", "read"]

""" for action in actions :
      for name in names: 
            print(name, actions) """
      

for name in names :
      for action in actions: 
            print(name, action)