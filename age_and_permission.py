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
