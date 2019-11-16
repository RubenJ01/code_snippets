"""
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extra:
1: Randomly generate two lists to test this
2: Write this in one line of Python
"""

# using the random module to generate some random lists
import random

# generating random lists with 10 entries between 1, 100 using randint
a = [random.randint(1, 100) for x in range(10)]
b = [random.randint(1, 100) for x in range(10)]

# using list comprehension to find the equal numbers
[print(x) for x in a for y in b if x == y]

__author__ = "Ruben Eekhof"
