"""
Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.

Extra:
1: Write two different functions to do this - one using a loop and constructing a list, and another using sets.

2: Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

# initializing the lists we will be using.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def loop_new_list(a, b):
    # create a new list with unique numbers from list a and b
    new_list = []
    for x in a:
        for y in b:
            if y != x:
                if x in new_list or y in new_list:
                    pass
                else:
                    new_list.append(x)
                    new_list.append(y)
    return new_list


def set_new_list(a, b):
    # initializing our new list
    new_list = []
    # combining list a + b into new_list
    new_list.extend(a+b)
    # turning new_list into a set so all duplicates will be removed
    new_list = set(new_list)
    # turning new_list back into a list
    new_list = list(new_list)
    return new_list


# printing the output of both functions
print(set_new_list(a, b))
print(loop_new_list(a, b))

__author__ = "Ruben Eekhof"
