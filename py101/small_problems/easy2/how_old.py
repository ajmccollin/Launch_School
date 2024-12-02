from random import randint

name = input('What is your name? ')
age = randint(20,100)

if len(name) > 0:
    print(f'{name} is {age} years old!')
else:
    print(f'Teddy is {age} years old!')
