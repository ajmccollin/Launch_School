bill_amount = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

tip_amount = bill_amount * (tip_percentage * .01)
total_amount = tip_amount + bill_amount

print(f'The tip is ${tip_amount}')
print(f'The total is ${total_amount}')