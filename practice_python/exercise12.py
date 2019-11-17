"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

# initializing the list we will be using
a = [5, 10, 15, 20, 25]

# creating a new list with the first and last element by checking if the index is either the first or last
# the first index is always 0
# the last index is the length of the array - 1 as indexing starts with 0 and counting with 1
new_list = list([x for x in a if x == a[0] or x == a[len(a) - 1]])

# printing our new list
print(new_list)

__author__ = "Ruben Eekhof"
