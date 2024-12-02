#Ask user to enter integer greater than 0
#Ask user if they want to add or multiply
#Return either product or sum of consecutive numbers
def multiplication(user_num):
    result = 1
    for num in range(1, user_num):
        result *= num
    return result

def addition(user_num):
    result = 0
    for num in range(1, user_num):
        result += num
    return result

user_num = int(input('Please enter a integer greater than 0: '))

print('Enter "s" to compute the sum, or "p" to compute the product.')
operation = input()

if operation == 'p':
    result = multiplication(user_num)
    print(f'The product of the integers between 1 and {user_num} is {result}')
elif operation == 's':
    result = addition(user_num)
    print(f'The sum of the integers between 1 and {user_num} is {result}')
else:
    print('Not a valid operation')

