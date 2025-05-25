'''
Given the following data structure return a new list identical in structure to 
the original, but containing only the numbers that are multiples of 3.
Expected result: 

[[], [3, 12], [9], [15, 18]]

'''


lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def only_odds(sublist):
    new_lst = [num for num in sublist if num % 3 == 0]
    return new_lst

odd_lst = [only_odds(sublst) for sublst in lst]
print(odd_lst)