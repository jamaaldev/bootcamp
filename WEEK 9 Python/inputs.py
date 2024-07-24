# Input

# Input, Process, Output

# print() is the basic output function
"""
print("This is an Output function")
print("Hello world 2.")
print("have a nice day.")


# input() is the basic Input function.

# userInput = input("Enter Some Text: ") # waits for the input from a user, before resuming code/execution

# print(userInput)


# Excercise
# 1.) Create 3 variables and take input: firstName, lastName, Age and let the user enter them.
# 2.) Display a welcome message: output their names and age back to the console
# 3.) Create a addition calculator: Take 2 numbers, add them and display the result back.

firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
age = input("Enter your age: ")



# Excercise 2

print("Welcome human " + firstName + " " + lastName + " " + "How old you are: " + age)
print("welcome human", firstName, lastName, "you are", age, "years old.")
"""

# Excercise 3: basic Addition calculator
"""
num1 = 20
num2 = 300
"""

num1 = input("Enter first Number: ")
num2 = input("Enter Second Number: ")

# input() always results in a String Data type.


# Convert a variable to an Integer (number) Data Type.
# use the int()

num1 = int(num1)
num2 = int(num2)


print(num1 + num2)


