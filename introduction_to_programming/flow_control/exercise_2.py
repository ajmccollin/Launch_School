def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

user_number = int(input('Please enter an integer: '))

even_or_odd(user_number)