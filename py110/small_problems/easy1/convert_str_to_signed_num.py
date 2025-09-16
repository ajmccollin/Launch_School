'''
P - Create a function that takes a string and returns an integer, whether - or +
E -  E: Cannot use build in int function
        If there is a + or a -, return positive or negative respectively.
        If there is not a sign for either, return positive.
        Number will always be valid.
        Use function from prev. exercise.
    IQ: 
D -  I: String
     O: Intger with leading + or =
     N: Might want to create a conditional after the fact to sort. 
A - Adjust the function so it only takes in a char if it is a digit.
    If input argument at index 0 is -, return a formatted string beginning w/ -
    If input argument at index 0 is +, return an f-string beginning with +
'''
DIGITS = {
    '1': 1, 
    '2': 2, 
    '3': 3,
    '4': 4, 
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
}

def string_to_signed_integer(input_str):
    count = 0

    for char in input_str:
        if char.isdigit():
            count = (10 * count) + DIGITS[char]
    
    if input_str[0] == '-':
        return -count
    return count
    
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True