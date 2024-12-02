def multiply(left, right):
    product = left * right
    return product

def get_number(prompt):
    input_value = input(prompt)
    return float(input_value)

num1 = get_number('Enter a number: ')
num2 = get_number('Enter another number: ')
product = multiply(num1, num2)

print(f'{num1} * {num2} = {product}')

