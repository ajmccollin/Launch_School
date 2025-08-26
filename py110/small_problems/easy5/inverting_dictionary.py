'''
P - Create a function that swaps the keys and values, so the values become the
    keys and the keys become the values. 
E - E: Keys and values are unique.
        - Need to switch keys/ values
    I: Input will always be vald. 
D - I: dictonary
    O: dictionary inverted
A - 1. Create a function called `invert_dictionary` that takes input_dict
        as a parameter.
    2. Create a variable called keys and set equal to input_dict.keys()
    3. Create a variable called values and set equal to input_dict.values()
    4. zip the pairs, values first then keys. 
    5. call the dict function and return.
'''
def invert_dict(input_dict):
    dict_keys = input_dict.keys()
    dict_values = input_dict.values()
    return dict(zip(dict_values, dict_keys))

'''
def invert_dict(input_dict):
    return {value: key for key, value in input_dict.items()}''' # more concise

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True