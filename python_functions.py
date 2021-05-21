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




