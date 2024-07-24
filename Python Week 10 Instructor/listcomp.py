# List Comprehension

# a Squared number: num * num: 2 * 2 = 4,  3 * 3 = 9, ....

squareNums = [] 

# Manually: Type it in
# Iteration: for loop
# Comprehension: consise, easier way

x = 10

for i in range(x):
	# squareNums.append(i ** 2) # Exponentiation Operator (x ** power)
	squareNums.append(i * i)
	print(squareNums)


# Building a List with List Comprehension
"""
Syntax
list = [1(expression)1(for)0*(ifs/fors)]

"""

print("\nUsing List Comprehension:")


seq = [i for i in range(x)]
print(seq)


squareNums2 = [(i ** 2) for i in range(x)]
print(squareNums2)


seq2 = [(i) for i in range(x)]
print(seq2)


seq3 = [i for i in range(20) if i > 10]
print(seq3)


# Example with 2 lists: Find Common Items between the lists
print("\nFinding Common Numbers between 2 lists:")
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [5, 6, 7, 8, 9, 10, 11, 12, 13]

listCommonAB = [a for a in listA if a in listB]
print(listCommonAB)


listC = [[i, i] for i in listA]

"""
[i for i in listA]

==

for i in listA:
	return i
"""


# tuple = (10, 20, 30)

print(listC)

# listD = [["apple", "banana", "cranberry"] for i in range(20)]
# print(listD)


