"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extra:
1: If the number is a multiple of 4, print out a different message.

2: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

# asking the user for a number
number = int(input('Number: '))

# checking if the number is a multiple of 4 by dividing it by for and checking if its still an int
if number / 4 == int(number / 4):
    print(f"{number} is a multiple of 4.")
# checking if the division of the number is equal to a float or an int
# because 5/2 = 2.5 and thus a float and an odd number
elif number / 2 == int(number / 2):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# getting the required inputs
num = int(input('Check: '))
check = int(input('Divide by: '))

# checking if the numbers divide evenly
if num / check == int(num / check):
    print(f"{num}/{check} divide evenly.")
else:
    print(f"{num}/{check} doesnt divide evenly.")

__author__ = "Ruben Eekhof"
