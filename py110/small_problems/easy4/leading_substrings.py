'''
P - Create a function that takes a string as an argument and returns a list of
    substrings beginning with the first letter, ordered shortest to longest.
    
    Input: String
    Output: list of strings
    Explicit: start with first letter return the substrings
        - shortest to longest substrings
    Implicit:
        - Input will always be valid
D - Output will return a list of strings
A - 1. Define a function called `leading_substrings` that takes the parameter 
            string
    2. Create a return list to store substrings in
    3. Iterate over each char from a range in a string.
        (for num in range(0, num)) and append to the empty list.
    4. Return empty list

'''
def leading_substrings(input_str):
    return [input_str[0: idx] for idx in range(1, len(input_str) + 1)]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])