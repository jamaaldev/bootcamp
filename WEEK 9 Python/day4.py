# Excercises on functions- 
# - Write a function that will Cube a Number. Take a single parameter and return the cube (x^3)
# - Write a function that will add 2 numbers together. the function will take 2 parameters and return the sum of them.
# - write a function that will find the average of 3 numbers. the function should take 3 parameters and then return the average (sum / 3)
# - Write a function that takes a list of numbers, iterates through it and finds the total sum of the list.

from time import sleep



def numberCube(cube):
    return cube * cube * cube

sleep(2)
print('Cube a Number',numberCube(2))

def numberAdd(num1,num2):
    return num1 + num2

print('add 2 numbers together.',numberAdd(5,7))

def findAvg(a,b,c):
    return a+b+c / 3

print('find the average of 3 numbers.',findAvg(5,2,3))

def numberList(list):
    sum = 0
    for numbers in list:
       sum += numbers
    return sum
print('list of numbers',numberList([1,2,3,5,8,9]))