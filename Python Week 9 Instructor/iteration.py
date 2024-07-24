# Iteration
# Looping, repeating code

"""
for loops
defintite iteration

for variable in range():
	indented-code which will repeat a number of times.
"""
# iterating with range()
for i in range(10):		 	# range(endpoint)
	print("hello world", i)

for i in range(5, 10): 		# range(starting, endpoint)
	print("hello world", i)

for i in range(5, 10, 2): 	# range(starting, endpoint, step/increment)
	print("hello world", i)



# iterating through a collection (list)
# for element in collection:

basket = ["orange", "apple", "melon", "lychee", "papaya"]

for element in basket:
	print(element)



"""
while loops

indefinite iteration

while condition:
	indented code-block



x = 0

while x <= 10: # while loops can potensially run forever
	x = x + 1
	print("hello world", x)


# Ex 1.) String Repeater: create a program that will repeat print a number of times: let the user input both the string and the number of times they'd like to repeat it.

userString = input("Enter a string to repeat: ")
repeater = int(input("How many times would you like to repeat it? "))

for i in range(repeater):
	print(userString)


"""

# Ex 2.) Create a program that will ask the user to guess a passcode.
# should keep on asking contiously until they get it right.
# set a passcode variable
# let the user enter a guess at the passcode
# check if they got it right or wrong: loop continously until they get it right.

passcode = "pass123"


userInput = input("Enter the passcode: ")

while userInput != passcode:
	userInput = input("Wrong, Try again: ")

print("access granted")
