def calculate_sum(user_number):
    sum = 0
    for num in range(1, user_number + 1):
        sum += num
    return sum

def calculate_product(user_number):
    product = 1
    for num in range(1, user_number + 1):
        product *= num
    return product

while True:
    try:
        user_number = int(input('Please enter an integer greater than 0: '))
        if user_number > 0:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print('Enter "s" to compute the sum, or "p" to compute the product.')
sum_or_product = input()

while sum_or_product not in ['s', 'p']:
    print("Please enter 's' to compute the sum, "
          "or 'p' to compute the product.")
    sum_or_product = input()
if sum_or_product == 's':
    total_sum = calculate_sum(user_number)
    print(f"The sum of integers between 1 and {user_number} is {total_sum}.")
elif sum_or_product == 'p':
    total_product = calculate_product(user_number)
    print(f"The product of integers between 1 and {user_number} "
          f"is {total_product}.")
else:
    print("Hmm, something went wrong")