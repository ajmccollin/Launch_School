import time
import json
with open('mortgage_messages.json', 'r') as file:
    MESSAGE = json.load(file)

def prompt(message):
    print(f'==> {message} ')

def invalid_number(user_number):
    try:
        number = float(user_number)
        if number <= 0:
            raise ValueError("Number must be greater than 0")
    except ValueError:
        return True
    return False

prompt(MESSAGE['welcome'])

calculate = True
while calculate:
    prompt(MESSAGE['loan_amount'])
    loan_amount = (input('$'))

    while invalid_number(loan_amount):
        prompt(MESSAGE['invalid_number'])
        loan_amount = input('$')

    prompt('What is your loan duration (in years)? ')
    yearly_duration = input()

    while invalid_number(yearly_duration):
        prompt(MESSAGE['invalid_number'])
        yearly_duration = input()

    prompt('What is your Annual Percentage Rate (APR)? ')
    prompt('Enter 18 for 18%, 7 for 7%, etc... ')
    annual_rate = input()

    while invalid_number(annual_rate):
        prompt(MESSAGE['invalid_number'])
        annual_rate = input()


    monthly_rate = (float(annual_rate) / 100) / 12
    monthly_duration = float(yearly_duration) * 12

    monthly_payment = float(loan_amount) * (
        monthly_rate / (1 - (1 + monthly_rate) ** (-monthly_duration))
    )

    prompt(f'Your monthly payment is ${monthly_payment:0.2f}')
    time.sleep(1.5)
    prompt('Would you like to calculate something else? Y/N? ')
    recalculate = input()

    while recalculate not in ['Y', 'N']:
        prompt('Please enter Y or N ')
        recalculate = input()
    if recalculate == 'Y':
        continue
    elif recalculate == 'N':
        prompt('Thank you for using this calculator. Goodbye! ')
        calculate = False