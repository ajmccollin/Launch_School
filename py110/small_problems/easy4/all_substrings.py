'''
P - Create a function that returns a list of all substrings of a string.
E - I: string
    O: list of substrings from input string
    E: all substrings of a string should be returned within a list
      - shortest to longest
      - should use the leading_substrings function from prev exercise.
    I:
D - List 
A - 1. Paste leading_substrings() function from previous exercise.
    2. Create a function called substrings that takes a single string as 
        a parameter.
    3. Iterate over each character, from idx to len of string, calling 
        leading_substrings() function and return
'''
def leading_substrings(input_str):
    return [input_str[0: idx] for idx in range(1, len(input_str) + 1)]

def substrings(input_str):
    list_of_lists = [leading_substrings(input_str[idx:]) 
            for idx in range(len(input_str))]
    return [item for sublist in list_of_lists for item in sublist]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True