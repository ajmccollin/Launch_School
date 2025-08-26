'''
P - Create a function that takes a list of strings and returns a list of 
    strings with vowels removed. 
E - E:  - vowels are a e i o u
        - if vowels are in string, return a new string without vowels
    I:
D - I: List of strings
    O: List of new strings without vowels
A - 1. Create a constant variable called VOWELS assigned to a e i o u
    2. Create a function called remove_vowels that takes a list as a parameter
        and create an empty string called expected_string
    3. Iterate over each string in the list, 
    4. Iterate over each char in the string and add character to expected_string
        if it is not in VOWELS
    5. return expected string or turn into comprehension.
'''
VOWELS = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

def remove_vowels(input_list):
    expected_list = []

    for string in input_list:
        expected_str = ''
        for char in string:
            if char not in VOWELS:
                expected_str += char
        expected_list.append(expected_str)
    return expected_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True