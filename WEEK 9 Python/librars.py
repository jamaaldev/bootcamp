from math import sqrt
from random import randint,random


userNumber = int(input('enter a number '))
print('sqaure root',sqrt(userNumber))

userNum1 = int(input('enter a number first '))
userNum2 = int(input('enter a number second '))
print(randint(userNum1,userNum2))

userName = input('enter your name please ')
randomID = str(random())
print('userID is',userName+randomID)
