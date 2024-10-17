numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
half_numbers = []

for values in numbers.values():
    number = values // 2
    half_numbers.append(number) # or .append(values // 2)

print(half_numbers)