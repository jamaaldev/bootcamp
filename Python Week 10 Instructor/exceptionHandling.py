# Exception Handling
import logging

logging.basicConfig(
	level = logging.DEBUG, 
	filename = "errors.log"
	#format = "%(levelname)s : %(asctime)s - %(message)s"
)

"""
To Do Exception handling we use:

try:
	block code
	block code
	block code
	block code
except:
	block code
	block code

Attempt our potentially ridden code with Try statement
Python wont crash the program and go to the Except Statement

"""
print("Hello world")
"""
x = 10
y = "Johnson"
print(x + y)

"""	

try:
	x = 10
	y = int(input("Enter a Number to add."))
	print(x / y)
except ValueError as err:
	print("You cant type a string....", err)
except ZeroDivisionError as err:
	print("You cant Divide by zero!!")
except Exception as err:
	print("Another error has Occured.")


print("here is the rest of the Code")
print("Goodbye World")