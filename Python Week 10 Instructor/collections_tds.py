# Collections
# Tuples, Dictionaries and Sets

""" More general functions
len() - Returns the Length
min() - Returns the minimum value of a collection
max() - Returns the maximum value of a collection


# List (Mutable)
myList = [10, 20, 30, 40, "bread", "rice"]

"""
# Tuple (Immutable)
# Immutable: cannot add or remove values from the collection
# Defined by a round bracket.
myTuple = (10, 20, 30, 40, "round", "square")



print(len(myTuple))

myTuple[1] = 20

# print(min(myTuple))
# print(max(myTuple))

# Dictionary
# Are similar to Objects in JavaScript
# Key-Value Pair
# Key:Value

"""
dictionaries start with a Curly Brace.

dictionary = {
	key: value
}
"""
# You'll see this pattern in *.json File Types
"""
person = {
	"firstName": "Bob", 
	"lastName": "Johnson",
	"age": 25,
	"bio": "A Straight-Forward and Effective Man"
}

# Outputting a Dictionary
print(person)

# Accessing a Dictionary

# How to access "Bob"?
# access a dictionary like you would other collections: list[index] tuple[index] dict[key]
print(person["firstName"])
print(person["lastName"])
print(person.get("firstName"))
print(person.get("address", "10 Pivot Lane"))

# Updating Values
person["age"] = 26
person.update({"age" : 26})

print(person)

# Adding/Removing Values
# Adding
person.update({1: "Test"})
print(person)

# Removing
person.pop("bio")
del person["age"]

print(person)


"""
# Sets
# Unordered/Unindexed, Unchangeable, Unique.
# Unique: Will eliminate Duplicate Values
# Unchanageable: Cant update values.
# Unordred/Unindexed: There is no order with these sets. 

mySet = {"a", "b", "c", 10, 23, 40, 10, 50, 40, "a", 23, 62, "b", "z", "x", "c"}
print(mySet)

# Accessing Sets
findItem = "a"

print(findItem in mySet)

if findItem in mySet:
	print("This is true")

# Add/remove items from sets.

mySet.add(20424094)
mySet.discard("z")

mySet.pop() # Removes the "Last" item from the set, but Sets are random

print(mySet)