def number_range(number):
    if number <= 0:
        print(f'{number} is less than 0')
    elif number <= 50: 
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 50 and 100')
    else:
        print(f'{number} is greater than 100')
    
user_num = float(input('Please enter a number: '))
number_range(user_num)
