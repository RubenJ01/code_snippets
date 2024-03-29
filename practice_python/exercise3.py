"""
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extra:
1: Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.

2: Write this in one line of Python.

3: Ask the user for a number and return a list that contains only elements from the original
list a that are smaller than that number given by the user.
"""

# creating the lists we will be working with
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# requesting the user for a number
number = int(input('Number: '))

# creating a new list in 1 line that contains numbers of a that are lower then the requested number.
# this is equal to:
# for x in a:
#    if x < number:
#        print(x)
print([x for x in a if x < number])

__author__ = "Ruben Eekhof"


