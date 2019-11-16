"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extra:
1: Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message. (Hint: order of operations exists in Python)

2: Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""
# with this module we can get the current year
import datetime

# get the current year from the datetime module
current_year = datetime.datetime.now().year

# request the required data to run the program
name = input('Name: ')
age = int(input('Age: '))
repeat = int(input('How much times do you want to repeat the output: '))

# calculating specific data
years_till_100 = 100 - age
year_when_100 = current_year + years_till_100

# telling it to repeat itself as much times as the user requested.
for _ in range(repeat):
    # formatting the output of the program
    print(f"Hi {name}. You will turn 100 in {years_till_100} years! That's in {year_when_100}. \n")

__author__ = "Ruben Eekhof"
