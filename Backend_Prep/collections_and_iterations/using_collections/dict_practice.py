phone_numbers = {
    'John': '123-1234',
    'Steve': '131-1313',
    'Joanna': '998-9988',
    'Meghan': '654-3210',
}

print(phone_numbers.keys())
print(phone_numbers.values())
print(phone_numbers.items())

del phone_numbers['John']
del phone_numbers['Steve']

print(phone_numbers.items())

phone_numbers['Max'] = '333-3333'

print(phone_numbers.items())
