ORDINAL_NUMBERS = ['1st', '2nd', '3rd', '4th', '5th']

def get_valid_integer(prompt_message):
    while True:
        try:
            user_num = int(input(prompt_message))
            return str(user_num)
        except ValueError:
            print("That is not a valid number! Please enter a number: ")

list_of_nums = []

for num in ORDINAL_NUMBERS:
    user_num = get_valid_integer(f'Enter the {num} number: ')
    list_of_nums.append(user_num)
num_check = get_valid_integer('Enter the last number: ')

if num_check not in list_of_nums:
    print(f"{num_check} isn't in {', '.join(list_of_nums)}.")
else:
    print(f"{num_check} is in {', '.join(list_of_nums)}.")

if any(int(num) > 25 for num in list_of_nums):
    print('There is at least one number that is greater than 25!')
else:
    print('None of these numbers are greater than 25')