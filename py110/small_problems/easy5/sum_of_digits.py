'''
P - Create a function that takes a single positive integer as an argument and returns the sum of those digits.
E - E: The argument will be a single integer
    I: The argument will always be valid.
D - I: An integer
    O: Also an integer
    N: Might want to covert to string, iterate, and sum
A - 1. Define a function `sum_of_digits` that has the parameter `input_integer`
    2. Convert the integer to a string and iterate over each number of the string.
    3. Return the sum of each iteration and store to a variable.
'''
def sum_digits(input_integer):
    digits = [int(num) for num in str(input_integer)]
    return sum(digits)
    

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True