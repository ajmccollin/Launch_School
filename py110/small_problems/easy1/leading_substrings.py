'''
P - Create a function that returns a list of substrings from an input 
    string starting with the first letter and gradually adding each letter.

E - Each string should begin with the first letter of the word.
  - The list should be ordered from shortest to longest. 

D - Input: String
  - Output: List of substrings

A - 1. Define a function called `leading_substrings` that takes the parameter 
        `string`
    2. Create an empty list called `substring_list`
    3. Iterate over each index, starting from 0 to 0, then adding 1 to the end
        range until the index is equal to the length of the string.
    4. Append each element to `substring_list`
    5. Return `substring_list`

C -
'''

def leading_substrings(string):
    return [string[0: index] for index in range(1, len(string) + 1)]
    
    # index = 1

    # while index <= len(string):
    #     substring_list.append(string[0:index])
    #     index += 1

    # return substring_list

    

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])