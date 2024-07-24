"""
Author: RL
Date: 2023-02-20
Time: 30 Minutes

Read the Questions and Answer Them as best as you can.

"""

### Excercise 1
"Given NumListA, Write code that will iterate through the list and find the Total Sum of the list"
numListA = [2, 20, 10, 30, 20, 40, 51, 32, 20]
def mySum(num):
    Sum = 0
    for i in num:
        Sum += i
    return Sum 
print('outside',mySum(numListA))

### Excercise 2
"This Program will Let the User Build list and print it."
"The program should first ask the user how long they want the list to be, then let them keep on entering values until its full."

# Un-Comment and Complete the program below, filling in the gaps (???)

List2 = []
listLength = int(input("How long do you want the list to be?"))
for i in range(listLength):
	userInput = input("what would you like to enter")
	List2.append(userInput)

print(List2)
	
### Excercise 3
"Given a Value and a quantity, Write Code that will generate a list that repeats the same item, by the quantity Specified"
val = "apple"
quantity = 5

for i in range(quantity):
    print('apple',val)

### Excercise 4
"Given a List of Strings, Write Code that will reverse Each of the strings Inside the list."
List4 = ["Melon", "Banana", "Apple", "Cherry"]
listrev = []
List4.sort(reverse=True)
for i in List4:
    listrev.append(i[::-1])
print(listrev)
### Excercise 5
"Given the List of Strings, Complete the code so that the program will Count the number of times a string in the list Starts with a given Prefix."
# Hint: use the startswith() function
List5 = ["car", "dog", "cat", "tree", "cattle", "bush", "camera"]
prefix = "ca"
count = 0
for i in List5:
    if i.startswith(prefix):
        count+= 1
print(count)
# Complete the Program