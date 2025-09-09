'''
P - Create a function that returns the sum of each subsequence for a list of numbers in a list.
E - E: Start at the first integer of the list and then continually add the next integer.
    - Return one integer, the sum of these sequences.
    - List contains integers?
    I: The list always contains one number and the input will always be valid. 
D - I: List of integers
    O: One singular integer.
    N: Sum function might be helpful.
       Will need to interate over each number in the list.
A - 1. Define a function called `sum_of_sums` that takes the parameter `input_list`.
    2. Iterate over each element in the list
    3. Return the sum from the first element of the list to an index. 
    4. Increase index and repeat. 
    5. Save to a variable and add all the numbers together.
'''
def sum_of_sums(input_list):
    total = 0
    sublists = [input_list[0: idx] for idx in range(1, len(input_list) + 1)]
    for num in sublists:
        total += sum(num)
    return total



print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True