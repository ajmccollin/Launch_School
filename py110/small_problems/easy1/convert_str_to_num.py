'''
P - Create a function that converts a string to integers without using the 
        int function.
E -  E: Cannot use the int function.
        All values are valid.
     IQ:
D -  I: String
     O: The string converted to an integer without use of int function.
     N: Store str as dict keys assigned to int values
        Have a count equal to 0 that you add values to based on dict value. 
A -  1. Create a Constant variable called digits that is a dictionary. 
            Each value in the diction is a string key with integer value. 
            ('1': 1, '2': 2, etc. )
     2. Define a function called string_to_integer that takes a string as an    
            argument.
     3. Set a variable count equal to 0 and iterate over each char in the input
             string
     4. Access the value associated to each key for each iteration and add
            it to the count variable.
     5. Return count variable. 
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

def string_to_integer(input_str):
    count = 0

    for char in input_str:
        count = (10 * count) + DIGITS[char]

    return count

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True