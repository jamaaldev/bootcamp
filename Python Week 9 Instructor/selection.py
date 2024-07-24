# Selection
# If Statements
# Control the flow of code in our program.
# IF a condition is true, then we execute some code.

"""
## Basic If-Statement

if condition:
	indented-codeblock
	indented-codeblock
	indented-codeblock
	indented-codeblock
	indented-codeblock
normal de-indented code
normal de-indented code
normal de-indented code
normal de-indented code

This is javascripts If statement
if (condition) {
	codeblock
}

"""

"""
Conditional Operators
use these to build a condition.
>	Greater Than
<	Less Than
==	Equal to
<=	Less than or equal to
>=	Greater Than equal to
!=	Not Equal to


x = 30

if x > 10:
	print("Hello, World!")

print("Some more lines of code here.")

"""
"""

## If-Else Statement
If the condition isnt met, then we can run some alternative code

if condition:
	indented-codeblock
else:
	indented-codeblock, if the intital condition isnt met

y = 5
if y > 10:
	print("Hello, World!")
else:
	print("Goodbye, World!")

print("Some more lines of code here.")


"""


"""
## If-Elif  (If Else-If) Statement

If the condition isnt met, then we can run some alternative code

if condition:
	indented-codeblock
elif condition:
	indented-codeblock, if the intital condition isnt met


"elif" is short for "else if"
"""

num = 0

if num > 0:
	print("This is a Positive Number")
elif num == 0:
	print("This is Zero")
else:
	print("This is a Negative Number")


# 3 Excercises (25 mins)
# Create a program that lets a user input their age, checks if they are old enough to vote (over 18)
"""
userAge = int(input("Enter your Age: "))

if userAge >= 18:
	print("You are Old enough to vote")
else:
	print("you are not old enough to vote")


# Create a program that lets a user enter 2 numbers. Compare them and print to the user:
# 	if the first is greater the other , 
# 	if the second is greater then the other
# 	or if they are both equal

num1 = int(input("Enter your first Number: "))
num2 = int(input("Enter your second Number: "))

if num1 > num2:
	print("Your first number", num1, "is greater then the second number", num2)
elif num2 > num1:
	print("Your second number", num2, "is greater then the first number", num1)
else:
	print("Number", num1, "and", num2 ,"are equal.")



# Create a program that lets a user enter their score between 0 and 100 and it will print their grade.
#	A: 80 - 100
# 	B: 60 - 79
# 	C: 40 - 59
# 	D: 20 - 39
# 	E: 0 - 19

userScore = int(input("Enter your Score (0-100): "))
grade = ""

if userScore >= 80 and userScore <= 100:
	grade = "A"
elif userScore >= 60 and userScore <= 79:
	grade = "B"
elif userScore >= 40 and userScore <= 59:
	grade = "C"
elif userScore >= 20 and userScore <= 39:
	grade = "D"
elif userScore >= 0 and userScore <= 19:
	grade = "E"
else:
	grade = "Invalid Entry"

print("Your final grade is: " + grade)

"""
# Extension: print if they've given an invalid score

"""
# Nested if Statements
if condition:
	if condition:
		code
	code

"""
userScore = int(input("Enter your Score (0-100): "))
grade = ""

if userScore > 100 or userScore < 0:
	print("invalid entry.")
else:
	if userScore >= 80:
		grade = "A"
	elif userScore >= 60:
		grade = "B"
	elif userScore >= 40:
		grade = "C"
	elif userScore >= 20:
		grade = "D"
	elif userScore >= 0:
		grade = "E"
	print("Your final grade is: " + grade)
