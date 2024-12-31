user_num1 = float(input('Enter the first number: '))
user_num2 = float(input('Enter the second number: '))

def calculate(number1, number2, operator):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case '/':
            return number1 / number2
        case '//':
            return number1 // number2
        case '%':
            return number1 % number2
        case '**':
            return number1 ** number2

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    output = calculate(user_num1, user_num2, operator)
    print(f'{user_num1} {operator} {user_num2} = {output}')
