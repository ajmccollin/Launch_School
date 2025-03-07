num1 = input('Please enter the 1st number: ')
num2 = input('Please enter the 2nd number: ')
num3 = input('Please enter the 3rd number: ')
num4 = input('Please enter the 4th number: ')
num5 = input('Please enter the 5th number: ')

num_list = [num1, num2, num3, num4, num5]
joined_list = ','.join(num_list)

final_number = input('Enter the last number: ')

if final_number in num_list:
    print(f'{final_number} is in {joined_list}')
else:
    print(f"{final_number} isn't in {joined_list}")