# Functions
# A function is simply a subroutine with a Return statement.

""" Creating a function

def identifier(parameters): # Input
	code-block
	code-block
	code-block
	code-block
	return statement 	# Output

code de-indented isnt a part of the Function

"""

def myFunction():
	return "Hello World"


myFunction() # "Hello World"

# myFunction = "hello world"


# Return is the evaluation of a function
# print(myFunction()) # print("Hello World")

variable1 = myFunction() # variable1 = "Hello World"
print(variable1)


def squareNumber(x): 	# Parameters act like an Input
	result = x * x		# Code acts as the Process
	return result		# Return acts as Output

myNum = squareNumber(7)

print(myNum)


"""
- Write a function that will Cube a Number. Take a single parameter and return the cube (x^3)

- Write a function that will add 2 numbers together. the function will take 2 parameters and return the sum of them.

- write a function that will find the average of 3 numbers. the function should take 3 parameters and then return the average (sum / 3)

- Write a function that takes a list of numbers, iterating through it and finds the total sum of the list.

"""
# EX1
def cubeNumber(x):
	answer = x * x * x
	return answer
	# return x * x * x


print(cubeNumber(5))

# EX2
def sumNumbers(x, y):
	return x + y


print(sumNumbers(50, 100))


# EX3
def findAverageOf3(x, y, z):
	total = x + y + z
	result = total / 3
	return result

print(findAverageOf3(45, 90, 180))

myList = [30, 342, 4, 21, 53, 523, 66, 21]

# EX 4
def totalSumList(listin):
	total = 0
	for num in listin:
		total = total + num
	return total

print(totalSumList(myList))


