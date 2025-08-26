'''
P - Create a function that produces a dictionary only if specific keys are 
        selected.
E - E: Only specific items should be returned based on if a key is in a 
        specific list. 
    I: The argument will always be valid
D - I: a dictionary
    O: a new dictionary with only specific items.
A - 1. Create a function called `keep_keys` that takes two parameters, the 
        input dictionary and the list of keys. 
    2. Iterate over each item in the dictionary, if dictionary.keys() in keys
        list, then return the item pairs. (comprehension)
'''
def keep_keys(input_dict, keys):
    return {key: value for key, value in input_dict.items() 
            if key in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys)) # == expected_dict) # True