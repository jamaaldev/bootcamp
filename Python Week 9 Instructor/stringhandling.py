# String Handling

# Making String Variable
"""
userString = "string" # Single-Line Strings

firstName = "bob"
lastName = "johnson" 

# Multi-Line String
myMutliLine0 = "This is a Single Line String.\nBackslash \\n will make a new line."
# print(myMutliLine0)
"""

myMutliLine1 = """
This is a Multi-Line String.
This will hold Multiple Lines.

Returns in.

The Return "\\n" is invisble in this case.
myString = "This is a String with \"Double Quotes\" in it"
myString = 'This is a String with "Double Quotes" in it'
"""

# Escape Characters, start with a "\" backslash.
# \n Makes a new line
# \t This will make a Tab space
# \\ This will write out a literal backslash




# Concatenating strings
firstName = "Bob"
lastName = "Johnson"

# Commas in a variable will just make a list.
# sentence = "Hello my name is ", firstName, " and my last name is ", lastName, "" 

# Only print allows concatenation with commas
print("using multiple arguements of print")
print("Hello my name is ", firstName, " and my last name is ", lastName, ".\n")
# print(firstName, lastName, ..., parameters)

#print(type(sentence))

print("using concatenation")
sentence = "Hello my name is " + firstName + " and my last name is " + lastName + ".\n"
print(sentence)

# f-strings (String Formatting)
# Put an f before the string
# Substitute variables in with {curlybraces}

print("using string formatting")
sentence = f"""
Hello my name is {firstName} and my last name is {lastName}.

This another sentence. i can continue typing right away.

"""
print(sentence)


# String Methods ####
myString = "Hello World!"

# Finding the Length of a String using len()

len(myString) # Returns the length of the string.

print(f"The length of '{myString}' is: {len(myString)}.")

# upper() will make strings uppercase.
print(myString.upper()) #

# lower() will make strings lowercase.
print(myString.lower())

# String Slicing
myString 		# Hello World!
myString[0] 	# Access an index[i] of a string
print(myString[0])


myString[3]
print(myString[3])

# Use the : colon sign to Slice Strings.

print(myString[4:]) # start at index 4 returns everything else infront

print(myString[:5]) # from beginning up to (but not including) 5
print(myString[1:5])

# Negative Indexing and Slicing
# Negative indexing means we start from the end.
myString = "Hello World!"
print(myString)
print(myString[-1]) # !
print(myString[-2]) # d
print(myString[-2:]) # 
print(myString[-6:]) # World!

long = "This another sentence. i can continue typing right away."
print(long[-1])
print(long[-5:]) # away.
# print(long[-11:]) # right away.


"""
## Excercises
Copy and Paste this sentence into a variable: "The quick brown fox jumps over the lazy dog"

1. Use Slicing to Return the word "jumps".
2. Use Slicing to return the words only "quick" and "fox", Combine them into one string.
3. Turn the Combined String into Upper Case.

4. Let the user enter their FirstName, LastName and Age. Using f-String Formatting, print their names and age in a welcome/greeting sentence.
5. Display the Full Name as Captialized Initials. Example: Oliver Rimmington > O. R
"""
# Ex 1
myString = "The quick brown fox jumps over the lazy dog"

print(myString[20:25])

# Ex 2
combined = f"{myString[4:9]} {myString[16:19]}"
print(combined)

# Ex 3
print(combined.upper())


# Ex 4
fname = input("Enter your firstName: ")
lname = input("Enter your LastName: ")
age = input("Enter your age: ")

greeting = f"Welcome {fname} {lname} you are are {age} years old. have a nice day."

print(greeting)

# Ex 5
print(fname[0])
print(lname[0])

intitals = f"{fname[0].upper()}. {lname[0].upper()}"
print(intitals)