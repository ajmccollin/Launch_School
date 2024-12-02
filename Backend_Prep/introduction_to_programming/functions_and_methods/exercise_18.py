def remainder_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainder_3(numbers_1))) #True
print(any(remainder_3(numbers_2))) #True
print(any(remainder_3(numbers_3))) #False
print(any(remainder_3(numbers_4))) #False