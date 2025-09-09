"""
P - Create a function that moves the first element of a list to the end.
E - E:  Needs to be a new list, not a mutated version of the original.
        Empty Lists return empty lists
        if the input is not a list, the output is None
    I: 
D - I:  - List of elements
    O:  - A new list of elements, with the first element at the end. 
    N:  - Append to append the first element to the end
        - Insert to insert elements before or insert first to the end?
        - Need to consider empty inputs and non-list inputs. 
A - 1. Define a funciton called `rotate_list` that has the parameter `input_list`
    2. Create an empty list called rotated_list. 
    3. Iterate over each element in the argument, from index 1 to the length of
        the input list, appending each element to the empty list.
    4. Finally, append the first element at index 0 to the end of `rotated_list`
    5. Return rotated list. 
    6. Set guard clauses for empty lists and non-list arguments.
"""
# def rotate_list(input_list):
#     if type(input_list) is list and len(input_list) > 0:
#         return input_list[1:] + [input_list[0]]
#     elif input_list == []:
#         return []
#     else:
#         return None
    
def rotate_list(input_list):
    if not isinstance(input_list, list):
        return None
    if len(input_list) == 0:
        return []
    return input_list[1:] + [input_list[0]]

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])