"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in
the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

# asking the users how much numbers we want to generate, -1 because each sequence starts with 1
amount = int(input('How much Fibonnaci numbers do you want to generate: '))

numbers = []

# using list comprehension to generate a list with Fibonnaci numbers with the requested amount
numbers = [1 if x in (0, 1) else numbers[x - 1] + numbers[x - 2] for x in range(amount)]

print(numbers)

__author__ = "Ruben Eekhof"