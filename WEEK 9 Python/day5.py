
sentence = "The quick brown fox jumps over the lazy dog"
# Done Task 1
jumps = sentence[20:-17]
print('Sentence: --> Jumps',jumps)
# Done Task 2 - 3
quick_fox =  f'{sentence[4:-33]}{sentence[16:-23]}'.upper()
print('Sentence: --> Quick and Fox',quick_fox)
# Done Task 4
firstName = input('enter your firstName ')
lastName = input('enter your lastName ')
age = int(input('enter your Age '))

greeting = f"Welcome {firstName} {lastName} Your Age is {age}"
print('Greeting',greeting)

# Done Task 5
fullNameFirstLatterCap = firstName[0].upper() + firstName[1:].lower() + ' ' + lastName[0].upper() + lastName[1:].lower()
print('FullNameFirstLatterCap',fullNameFirstLatterCap)