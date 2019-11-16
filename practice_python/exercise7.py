"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

# initializing the list we will be using
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# finding all the even numbers in the list
new_list = [x for x in a if x % 2 == 0]

# printing each list element using *
print(*new_list)

__author__ = "Ruben Eekhof"
