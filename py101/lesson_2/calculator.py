import json
with open('calculator_messages.json', 'r') as file:
    MESSAGE = json.load(file)


def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt(MESSAGE['welcome'])

calculate = True
while calculate:
    prompt(MESSAGE['first_number'])
    number1 = input()


    while invalid_number(number1):
        prompt(MESSAGE['invalid_number'])
        number1 = input()

    prompt(MESSAGE['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGE['invalid_number'])
        number2 = input()

    prompt(MESSAGE['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

    match operation:
        case '1':   # '1' represents addition
            output = float(number1) + float(number2)
        case '2':   #'2' represents subtraction
            output = float(number1) - float(number2)
        case '3':   #'3' represents multiplication
            output = float(number1) * float(number2)
        case '4':   #'4' represents division
            output = float(number1) / float(number2)

    prompt(f'The result is {output}')
    prompt(MESSAGE['recalculate'])
    
    recalculate = input()
    while recalculate not in ['Y', 'N']:
        prompt('Please enter Y or N ')
        recalculate = input()
    if recalculate == 'Y':
        continue
    elif recalculate == 'N':
        calculate = False
        


        
