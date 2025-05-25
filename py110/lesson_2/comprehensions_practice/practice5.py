'''
Given the following data structure, sort the list so that the sub-lists are
 ordered based on the sum of the odd numbers that they contain. You shouldn't 
 mutate the original list.

 Expected Output: 
 [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_sum(lst):
    odds = [num for num in lst if num % 2 == 1]
    return sum(odds)

sum_of_odds = sorted(lst, key=odd_sum)
print(sum_of_odds)