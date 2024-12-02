#prompt user for two positive float numbers
#print result of:
    #addition
    #subtraction
    #product
    #quotient
    #floor quoteint
    #remainder
    #power
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


user_num1 = float(input('Enter the first number: '))
user_num2 = float(input('Enter the second number: '))



for operator in ['+', '-', '*', '/', '//', '%', '**']:
    print(f'==> {user_num1} {operator} {user_num2} =' 
    f'{calculate(user_num1, user_num2, operator)}')