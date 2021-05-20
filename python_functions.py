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