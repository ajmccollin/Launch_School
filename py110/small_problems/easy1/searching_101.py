list_of_numbers = []

list_of_numbers.append(input('Please enter the first number: '))
list_of_numbers.append(input('Please enter the second number: '))
list_of_numbers.append(input('Please enter the third number: '))
list_of_numbers.append(input('Please enter the forth number: '))
list_of_numbers.append(input('Please enter the fifth number: '))
num_check = input('Please enter the last number: ')

if num_check not in list_of_numbers:
    print(f"{num_check} isn't in {', '.join(list_of_numbers)}")
elif num_check in list_of_numbers:
    print(f"{num_check} is in {', '.join(list_of_numbers)}")