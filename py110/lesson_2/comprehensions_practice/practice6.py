'''
Given the following data structure, return a new list identical in structure
 to the original but, with each number incremented by 1. Do not modify the 
 original data structure. Use a comprehension.

 Expected Result:
 [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_by_one(nested_dict):
    new_dict = [nested_dict[key] + 1  for key in nested_dict.keys()]
    return new_dict



incremented_lst = [increment_by_one(nested_dict) for nested_dict in lst]
print(incremented_lst)