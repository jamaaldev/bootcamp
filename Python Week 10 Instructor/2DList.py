# 2D List
# Two-Dimensional List

# Is basically a List within a List

"""
Method 1
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

2DList = [a, b, c]

## Method 2 
twoList = [
	[1, 2, 3], 	# Row 0
	[4, 5, 6], 	# Row 1
	[7, 8, 9]	# Row 2
]

"""
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

twoListA = [a, b, c]

print(twoListA[2][1])

twoList = [
	#0  1  2
	[1, 2, 3], 	# Row 0
	[4, 5, 6], 	# Row 1
	[7, 8, 9]	# Row 2
]

# Acesssing Numbers
print(twoList[1][1]) # 5

print(twoList[2][1]) # 8


# Updating Numbers

# Change 6 to 60
print(twoList[1][2])

twoList[1][2] = 60

print(twoList[1][2])