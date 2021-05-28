# Functions
Blocks of code that do something you may want to call on again. Generally functions should do one thing, and do it well.

DRY = DON'T REPEAT YOURSELF - this is important as if you can put something within a function and re-use it, then use it.

## Basic Functions

```python
# Let's create a basic function to greet
# Syntax def name():

# First iteration
def greetings():
    return "Welcome to Cyber Security! " #

print(greetings())

# Second iteration
def greeting_user(name):
    return "Welcome on board!"
print(greeting_user("Engineering 88"))

# Take user name as input() and display it back to them with a greeting message of your choice
def user_name():
    user_name = input("Hello, please enter your name -->")
    return (f"Hello, {user_name} !")
print(user_name())

# Creating a function that takes 2 args as ints
# Build a basic object Orientated Calculator
# phase 1: build a simple calculator class containing add, subtract, multiply, divide.
# phase 2: expand by creating:
# Divisible by method that returns true or false dependent on the outcome
class Basic_calculator:
    def add(value1, value2):
        return value1 + value2
    print(add(2, 3))

    def subtract(value1, value2):
        return value1 - value2
    print(subtract(2, 3))

    def multiply(value1, value2):
        return value1 * value2
    print(multiply(2, 3))

    def divide(value1, value2):
        return value1 / value2
    print(divide(2, 3))

    def divisible(value1, value2):
        return True if value1 % value2 == 0 else False
    print(divisible(2, 3))

# Work out and return the area of a triangle
base = int(input("Input the base : "))
height = int(input("Input the height : "))
area = base * height / 2
print("area = ", area)

# inch to cm converter
print("Input your height: ")
inches = int(input("Inches: "))
centimetres = round(inches * 2.54)
print("Your height is : %d cm." % centimetres)
```

## A Simple Program To Use Control Flow 
```python
# Simple program to use control flow
# - You can vote and drive
# - You can vote
# - You can drive
# - you can't legally drink but your mates/uncles might have your back (> 16)
# - You are too young, go back to school!
# - As a user I should be able to keep being prompted for input until I say 'exit'
def permission(age):
    if age < 16:
        return "Sorry, you are too young, wait until you are older!"
    elif age == 16:
        return "Try to obtain your licence!"
    elif age < 18:
        if drive:
            return "You can drive,"
        else:
            return "You cannot legally drink. \n Please refrain from this!"

    if age >= 18:
        if drive:
            return "You can vote and drive."
        else:
            return "You can vote"

while True:
    age = int(input("Hello, how old are you ? \n"))
    if age >= 16:
        d_licence = input("Do you have a driving licence? Yes/No \n")
        if d_licence == "Yes":
            drive = True
        elif d_licence == "No":
            drive = False
    print(permission(age))
```

## Create a Magic Number Game
```python
# User story 1 - As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# 2 - As a user, I should get feedback if my number is too high or too low so I can adjust my guess.
# 3 - as a user I should only be able to guess 3 times before a new number is generated
# 4 - as a user, I should be able to keep playing until I respond with exit
# 5 - as a user, I should be able to use exit in a sentence and still terminate the program

import random

number = random.randrange(1,51)
guess = int(input("Guess a number between 1 and 50: "))
guess_total=0

while guess != number:
    if guess < number:
        print("You need to guess higher, try again!")
        guess = int(input("\n Guess a number between 1 and 50: "))
    else:
        print("You need to guess lower, try again!")
        guess = int(input("\n Guess a number between 1 and 50: "))

print("Well done!, you guessed correctly!")



# extra 6 - as a user, when I terminate the program I should get a message thanking me for playing and the number of times I guesses and number of times I found the number.

# Extra 7 - as a user, I should be asked the highest number that can be used to generate a random number


# self five
```
