'''
P - Create a function that converts a integer to a string without using prebuilt
        python functions.
E -  E: Value is non-negative integer.
        May not use any built in python methods or functions.
    IQ:
D -  I: Integer
     O: String of said integer.
     N: Dictionary and concatenation of a variable assigned to an empty string.
A - 1. Create a Constant variable assigned to a dictionary with the characters
        0-9 assigned to their cooresponding str value.
        converted_int = input int.
    2. Assign a variable to an empty string. 
    3. set a variable called place_value equal to 1
    4. Set a while conditinal while place value is less than the input integer.
    5. num is equal to input_int modulo place_value * 10.
    6. subtract num from input int. 
    7. concatenate the key associated to num value // place_value 
    8. place_value *= 10
    9. Once done iterating, return str[-1]
'''
DIGITS = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    0: '0',
}
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'

# def integer_to_string(input_int):
#     output_str = ''
#     total_count = input_int
#     place_value = 1

#     if input_int == 0:
#         return DIGITS[0]
    
#     while total_count != 0:
#         num = total_count % (place_value * 10)
#         output_str += DIGITS[num // place_value]

#         place_value *= 10
#         total_count -= num

#     return output_str[::-1]

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True