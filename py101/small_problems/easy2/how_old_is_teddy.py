import random

user_name = input('What is your name? ')
age = random.randrange(20, 100)

if len(user_name) != 0:
    print(f'{user_name} is {age} years old!')
else:
    print(f'Teddy is {age} years old!')

