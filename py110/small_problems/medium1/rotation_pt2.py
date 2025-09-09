'''
P - Create a function that rotates the last `count` of numbers by moving the
        first of digit from the `count` to the end and shifting the rest of the
        numbers to the left. 
E - E: 
    I: The input will always be a valid integer.
D - I: Integer
    O: A new integer
    N: Indices will most likely be a pivotal part of this code.
       Will be switching from index `count` to length of the integer.
       Will need to convert the integer to a mutable collection, either string
        or list.  
A - 1. Define a function called `rotate_rightmost_digits` that takes two 
        parameters, `number` and `count`. 
    2. Create an empty string called `final_sequence`
    3. Convert the input integer to a string and iterate over each character.
        4. For characters from index 0 to count, concatenate to `final_sequence`
        5. For character from count to the end of the sequence, concatenate 
            from count + 1 to the end, then concatenate number at count. 
    6. Call the integer function on `final_sequence` and return the output.
'''

# def rotate_rightmost_digits(number, count):
#     num_str = str(number)
#     rotation_start_digit = len(num_str) - count
#     return int(num_str[:rotation_start_digit] + 
#                num_str[rotation_start_digit + 1:] + 
#                num_str[rotation_start_digit])

def rotate_string(string):
    return string[1:] + string[0]

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True