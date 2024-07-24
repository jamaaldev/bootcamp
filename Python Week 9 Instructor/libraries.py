# Libaries

# Some Functions that we'd like to use, need to be imported.
# We can import modules/functions from the Python Standard Library

# Use the "import" and "from" keyword to import modules from the standard library

from time import sleep
from random import randint, random # Use a Comma to import multiple things
from math import sqrt

# Asterisk (*) will import Everything from that module


# Sleep() is a function that will pause the execution of the code

"""

print("Hello world")
sleep(2)
input("Press Enter to continue...")

print("Welcome to Python Programming")
sleep(2)
print("Have a nice day")
print("Goodbye world.")

print(sqrt(49))


randint(0, 10) # Returns a random number between the range given.

# Excercises
# 1.) import math squareroot function(). let the user input a number and print the sqaure root of it.
userNum = int(input("Enter a number to Sqaure Root: "))
answer = sqrt(userNum)

print("The Square Root of", userNum, "is", answer)


# 2.) import random randint(x, y) let the user input 2 numbers, generate a random number between the range of those 2 numbers given. 

userNum1 = int(input("Enter the First Number: "))
userNum2 = int(input("Enter the Second Number: "))

print(randint(userNum1, userNum2))
"""
# 3.) Take a name from the user and generate a random number: make a concatentating their name and a random generated number.

userName = input("Enter your username: ")
randnum = randint(100, 999)

print(userName + str(randnum))