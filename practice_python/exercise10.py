"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
Write this in one line of Python using at least one list comprehension.
(Hint: Remember list comprehensions from Exercise 7).

Extra:
Randomly generate two lists to test this.
"""

# using the random module to generate some random lists
import random

# generating random lists with 10 entries between 1, 100 using randint
a = [random.randint(1, 100) for x in range(10)]
b = [random.randint(1, 100) for x in range(10)]

# creating a list with dupes out of the last 2 lists
new_list = [x for x in a for y in b if x == y]

# printing the new list
print(*new_list)

__author__ = "Ruben Eekhof"
