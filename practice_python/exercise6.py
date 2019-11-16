"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
# requesting the user for a string
palindrome = input('String: ')

# reversing the string and checking if they are the same
if palindrome[::-1] == palindrome:
    print(f"{palindrome} is a palindrome.")
else:
    print(f"{palindrome} isn't a palindrome.")

__author__ = "Ruben Eekhof"
