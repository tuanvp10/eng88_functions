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