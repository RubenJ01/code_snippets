"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extra:
1: Keep the game going until the user types “exit”

2: Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

# importing the random module
import random

# initializing required variables
continue_ = 'continue'
tries = 0
correct = 0


# defining the main program that will run until the user decides to exit
def main():
    # making tries, correct and continue global variables
    global tries
    global correct
    global continue_
    random_number = random.randint(1, 9)
    guess = input('Generated a random number between 1/9. Guess it: ')
    # detecting if the user wants to exit
    if guess == 'exit':
        continue_ = 'exit'
        print(f"You have taken {tries} guesses and got {correct} correct. Thanks for playing!")
    elif int(guess) == random_number:
        print(f"{random_number} is indeed the correct number.")
        # adding up the amount of guesses and correct answers
        tries += 1
        correct += 1
    else:
        tries += 1
        print(f"False. The correct answer was {random_number}")


# initializing the main game state
print("Type exit at any time to stop the program.")
while continue_ != 'exit':
    main()

__author__ = "Ruben Eekhof"
