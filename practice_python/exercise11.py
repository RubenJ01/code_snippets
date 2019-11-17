"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity
to practice using functions, described below.
"""

# request a number from the user
number = int(input('Number: '))


# defining the function that will check if the submitted number is a prime number
def is_prime(number):
    if number % 2 == 0 and number != 2:
        print(f"{number} is not a prime number.")
    else:
        # create a list with all numbers below number
        numbers = list(range(1, number))
        # getting all divisors of the given number
        divisors = [x for x in numbers if number % x == 0]
        # checking if the divisors list is empty and if so its not a prime number
        if divisors:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} isn't a prime number.")


# calling to the function
is_prime(number)

__author__ = "Ruben Eekhof"
