3 # Excercises (25 mins)
# Create a program that lets a user input their age, checks if they are old enough to vote (over 18)# Create a program that lets a user enter 2 numbers. Compare them and print to the user:
# if the first is greater the other ,
# if the second is greater then the other   
# or if they are both equal# Create a program that lets a user enter their score between 0 and 100 and it will grade the score#   A: 80 - 100#   B: 60 - 79#   C: 40 - 59#   D: 20 - 39#   E: 0 - 19# Extension: print if they've given an invalid score

# Done Task 1
# age = int(input('please enter your age by number '))

# if age > 17:
#     print('you can vote')
# else:
#     print('you cant vote becuase your are under 18 years old.')

# Done Task 2

# firstNum = int(input('please enter your first number '))
# secondNum = int(input('please enter your second number '))

# if firstNum > secondNum:
#     print('your First Input Number is', firstNum,'is the Greater then the second Input Number', secondNum)
# elif secondNum > firstNum:
#      print('your second Input Number is', secondNum,'is the Greater then the first Input Number', firstNum)
# else:
#      print('your First Input Number is', firstNum,'is equal to second Input Number', secondNum)

# Done Task 3
# scoreGrade = int(input('please enter your Grade by Number '))

# if scoreGrade > 100:
#     print('This score Grade is Invalid')
# elif scoreGrade < 0:
#     print('this score Grade is invalid')
# elif scoreGrade > 0 and scoreGrade < 19:
#     print('your Grade is E:',scoreGrade)
# elif scoreGrade > 19 and scoreGrade < 39:
#     print('your Grade is D:',scoreGrade)
# elif scoreGrade > 39 and scoreGrade < 59:
#     print('your Grade is C:',scoreGrade)
# elif scoreGrade > 59 and scoreGrade < 79:
#     print('your Grade is B:',scoreGrade)
# elif scoreGrade > 79 and scoreGrade < 100:
#     print('your Grade is A:',scoreGrade)

# Done Task 1
userString = input('please enter text any thing ')
userNumber = int(input('please enter number any thing '))

for i in range(1,userNumber+1):
    print(i,userString)

# Done Task 2
guessMe = input('please enter passCode Just Guess it see your luck. ')
answer = 'jamaal'

while answer != guessMe:
    guessMe = input('please enter passCode Just Guess it see your luck. ')
    if guessMe == answer:
        print('you guessed is right, you are genius the passCode is',answer)
        break
