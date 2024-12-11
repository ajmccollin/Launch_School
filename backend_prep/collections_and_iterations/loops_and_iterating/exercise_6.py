my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

numbers = []
for num in my_list:
    if num % 2 == 0:
        numbers.append('even')
    else:
        numbers.append('odd')

print(numbers)