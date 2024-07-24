"""
Different Types of Data to work with.

Strings:
"" (double quotes) 
'' (single quotes)

Strings are Text.

Numbers:
Whole Numbers (Integers)
100
240

Decimal Point Numbers (Float) (Floating Point Value)
20.20
49.50

Boolean Data Type:
True 	(1)
False	(0)


print("Hello World!") # Strings (Text)
print(5000) # Integars (Whole Numbers)
print(60.40) # Floats (Decimal Number)
print(True) # Booleans (True or False)

# Use the type() function to clarify the data type.

print(type(5000))

# Concatenating Strings
firstName = "bob"
lastName = "johnson"

print(firstName + " " + lastName)

# Converting Betweening Data Types

int()
float()
str()
bool()

# With Numeric variables we can perform some arithmetic.
# Arithmetic Operators
num1 = 7
num2 = 150
num3 = 3

print(num1 + num2) # Addition 			+
print(num2 - num1) # Subtraction		-
print(num1 * num2) # Multiplication		*
print(num2 / num1) # Division			/

#	 50    %   5 = 0
print(num1 / num3)
print(num1 % num3) # Modulus Division	% (Returns the remainder of a non-whole division)
# print(num1 ** num3)# Exponentiation 	** (Raise a number to the power of the other.)

# Floats

# Dividing numbers will alwayus return them as a float.
print(50 / 5)
print(type(50 / 5))

myFloat = 94.389349287
print(myFloat)
print("%.5f" % myFloat) # use the "%.Nf" to round the number to N significant figures

"""

# Lists
# A Type of "Dynamic" Data Structure

# Like a variable: identifier = []
# Use sqaure brackets to define a List

# Zero based Index
#		  0   1   2   3   4   5   6
myList = [10, 34, 40, 50, 63, 72, 56]

print(myList)
print(type(myList))

# Accessing Values from Lists
# We want to access 63:
print(myList[4]) # myList[4] = 63


# Adding a New values to lists
# Append and Insert

myList.append(100) # Append will add a new value to the end of a list.
print(myList)
myList.insert(0, 357)
print(myList)

# Removing values from a list

myList.remove(63) # Will remove the first occurance of the Specified value from the list
print(myList)