# Subroutines

# Subroutines allow us to group and reuse code
""" Creating a Subroutine

def identifier():
	code-block
	code-block
	code-block
	code-block
code de-indented isnt a part of the subroutine

"""
def greeting():
	print("Hello World")
	print("Welcome to Python Programming")
	print("Have a nice day")
	print("Goodbye world.")
# not inside the subroutine.


# Invoking the subroutine: Calling it. Running it. Launching it.
# greeting() # Invoke the Greeting() subroutine.

# Subroutines with parameters
""" Creating a parameterized subroutine

def identifier(parameter1, parameter2, parameter3, ... parameterN):
	code-block
	code-block
	code-block
	code-block
code de-indented isnt a part of the subroutine

"""
def greeting2(name):
	print("Hello ", name)
	print("Welcome to Python Programming")
	print("Have a nice day")
	print("Goodbye world and take care", name)

greeting2("Bob Johnson")