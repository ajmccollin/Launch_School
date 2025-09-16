'''
P - Create a function that converts an integer to a string.
E -  E: Includes negative numbers.
        Use function from previous exercise.
        May not use any build in python functions to convert int to str.
    IQ: Number will always be an integer, positive or negative.
D -  I: Integer, possibly with leading `-`
     O: String to represent input integer, possibly with leading -
     N: 
A - 1. Copy/paste function from previous exercise.
    2. Create an if statement, if input_int at 0 is `-`, return formatted str.
        If not, progress as normal.
'''
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'

def signed_integer_to_string(number):
    if number < 0:
        number *= -1
        return f"-{integer_to_string(number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return integer_to_string(number)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True