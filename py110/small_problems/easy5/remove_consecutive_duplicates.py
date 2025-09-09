'''
P - Create a function that removes repeated sucessive values in an integer 
        sequence.
E - E:  Repeated values are removed.
    I:  Sequence is a list
D - I:  Sequence of integers
    O:  Sequence of integers with repeated succesive values removed.
    N: Store a value, then check if the next value is the stored integer.
A - 1. Define a function called `unique_sequence` that takes input_list as the
        parameter.
    2. Create an empty_list called final_sequence.
    3. Iterate over each integer pair in the list.
    4. If the integer is not equal to the last element in final_sequence, 
        append it to `final_sequence`
    5. Return the final list.
'''
def unique_sequence(input_list):
    if not input_list:
        return []

    final_sequence = [input_list[0]]
    
    for num in input_list[1:]:
        if num != final_sequence[-1]:
            final_sequence.append(num)

    return final_sequence


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
print(unique_sequence([]))