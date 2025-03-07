bill_amount = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))

total_tip = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + total_tip

print(f'The tip is ${total_tip:.2f}')
print(f'The total bill is ${total_bill:.2f}')