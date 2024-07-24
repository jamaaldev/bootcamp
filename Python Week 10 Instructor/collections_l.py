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
"""
# Dynamic Data Structures

# List (Mutable)
myList = [300, 500, True, False]
# True = 1
# False = 0
#print(myList)
print(type(myList))

# Methods
# print(myList[2]) # Access lsits with the list[index] sqaure brackets
print(myList)

myList.insert(2, "apples")

print(myList)

Adding
myList.insert(index, value) Positional Parameters 
myList.append()

Removing
myList.remove()
myList.pop()

Other Functions
myList.index()
myList.count()

myList.sort()
myList.sort(key=Len) Keywords Parameters


myList.reverse()


myList.append(500)
print(myList)

print("List Sorted in Ascending order (by default):")
myList.sort()
print(myList)

print("List Sorted in Descending order")
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


# Sort() Function (Keyword vs Positional Parameters)
wordList = ["Rally", "Sights", "Zed", "Apples", "Grapes", "Fox", "Quarter", 299, 150, 92, 1, 39]


# Most other functions take Positional-Parameters
# function(arguement1, arguement2, arguement3, ....)
# remove(value)
# pop(index)
# insert(index, value)
wordList.pop()
wordList.insert(4, "Congo")

myTuple = (10, 20, 30, 40).count(20)
# Sort() uses Keyword-Parameters
# function(parameter=arguement, parameter=arguement, ...)
# sort(reverse=, key=)
# "key" parameter will determine How exactly we want to sort this list.
# "reverse" parameter will determine if its Ascending or Descending


wordList.sort()
# wordList.sort(key=len, reverse=True)


print(wordList)