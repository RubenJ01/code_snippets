"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

# requesting the number we want to find the divisors of
number = int(input('Number: '))

# create a list with all numbers below number
numbers = list(range(1, number))

# getting all the divisors of number by checking if dividing them has a remainder using %
print([x for x in numbers if number % x == 0])

__author__ = "Ruben Eekhof"
