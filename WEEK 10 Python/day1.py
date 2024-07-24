fullName = 'bob johnson'
vowels = 'aeiou'

for i in vowels:
    if i in fullName:
        print(f'the vowel {i} is in --> {fullName}')
   

# Collections
# Data types/structures that hold more then one value.
# Arrays, Lists, Tuples, Dictionaries And Sets 

# [value, "string", 10, True]
# Quotation marks define a "string"

import array as arr

# Arrays have to be imported to use.
# Typecodes: "i" integer, "f" floats
# Only hold 1 type of data
myArray = arr.array("i", [2, 30, 540, 10, 402, 40])


myString = "Hello World"
myNumber = 300

# Dynamic Data Structures

# List (Mutable)
myList = [300, 500, True, False]
# True = 1
# False = 0
print(myList)
print(type(myList))

# Methods
print(myList[2]) # Access lsits with the list[index] sqaure brackets
"""
Adding
myList.insert() 
myList.append()

Removing
myList.remove()
myList.pop()

myList.index()
myList.count()
myList.sort()
myList.reverse()

"""
myList.append(500)
print(myList)

print("List Sorted in Ascending order (by default):")
myList.sort()
print(myList)

print("List Sorted in Descending order (")
myList.sort(reverse=True) # Asc/Descing order
print(myList)

myWords = ["Rally", "Sights", "Zed", "Apples", "Grapes", "Fox", "Quarter"]
print(myWords)

print("Reversed Order list")
print(myWords.reverse())

print("Sorted Alphabetically")
myWords.sort()
print(myWords)


# Sort By Length of item
print("sort by Length of items")
myWords.sort(key=len)
print(myWords)

print("Sorted Alphabetically DESC")

myWords.sort(reverse=True)
print(myWords)




"""
# Tuple (Immutable)
myTuple = ("String", "test", "this is more text", "test", 201, 24, 504, True, False)
print(myTuple)
print(type(myTuple))

# Index()
print(myTuple.index("test"))	# 2
print(myTuple.index(False)) 	# 7

# count() returns the number occurances of a given 
print(myTuple.count("test"))

# len()
# print(myTuple.len())
print(len(myTuple))

"""

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

