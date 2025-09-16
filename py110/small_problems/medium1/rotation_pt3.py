'''
P - Create a function that rotates the digits of an integer.
        The first digit goes to the end and the other digits shift left.
        Then, the first digit stays in place, the second goes to the end, the 
            others shift left.
        Repeat this process until all digits are rotated. 
E - E: 
    I: Should probably build off previous exercise's code.
D - I: Integer
    O: Integer
    N: Number of rotations will be the length of the integer.
A - 1. Define a function called `max_rotation` with the parameter `input_int`.
    2. 
'''

def rotate_string(string):
    return string[1:] + string[0]

# def rotate_rightmost_digits(number, count):
#     number_str = str(number)
#     first_part = number_str[:-count]
#     second_part = number_str[-count:]
#     result_str = first_part + rotate_string(second_part)

#     return int(result_str)

# def rotate_rightmost_digits(number, count):
#     num_str = str(number)
#     rotation_start_digit = len(num_str) - count
#     return int(num_str[:rotation_start_digit] + 
#                num_str[rotation_start_digit + 1:] + 
#                num_str[rotation_start_digit])

def max_rotation():
    pass

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True