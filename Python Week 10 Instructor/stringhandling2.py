# More on String Handling
myString = "Hello World!"

# myString = ["H", "e", "l", "l" ....]
# List = [1, 2, 3, 4, 5, 6]

# for-in
# We can Iterate through a String as if it were a List (Collection) 

# A String is a collection of characters.

for letter in myString:
	print(letter)


# Searching through strings
# In is also a Conditional Operator
# !=

print(10 != 50) # True

print("e" in myString) # True
print("He" in myString) # True
print("ellz" in myString) # True

searchQuote = "I like to play golf"
myLetter = "p"

if myLetter in searchQuote: # in | not in
	print(f"{myLetter} is inside of the string: {searchQuote}.")
else:
	print(f"{myLetter} isnt inside of the string: {searchQuote}.")

if myLetter not in searchQuote:
	print(f"{myLetter} isnt inside of the string: {searchQuote}.")
else:
	print(f"{myLetter} is inside of the string: {searchQuote}.")

print()
# Excercise (10) Check if a vowel is inside of a name:
vowels = "aeiou"
name = "oliver rimmington" # any name
#vowels = ["a", "e", "i", "o", "u"]

# If and/or For statement?

for i in vowels:
	if i in name:
		print(f"the vowel {i} is inside of {name}.")

