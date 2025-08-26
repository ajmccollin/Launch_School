'''
P - Return a list of all substrings in a string, ordered starting at index 0
    ranging to the last index of the list. 

E - Output substrings must be ordered by those starting at index 0, then 1, etc.
  - Output substrings will also be ordered from sshortest to longest. 
  - Should use the funcion from the previous exercise.

D - Input: A string
  - Output: A list of substrings 

A - Define function from previous exercise to calculate the first letter.
  - Define a new function that takes string as the input.
  - Iterate over each letter in word, calling the original function and adding
        that to a list.
  - Return the new list. 

'''
def substrings(string):
        return ([string[starting_value: index] 
                 for starting_value in range(0, len(string))
                 for index in range(starting_value + 1, len(string) + 1)])

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde')) # == expected_result)  # True