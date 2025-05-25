'''Given the following data structure, return a new list with the same 
structure, but with the values in each sublist ordered in ascending order.
 Use a comprehension if you can. (Try using a for loop first.)'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected Result: [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

sorted_lst = [sorted(nested_lst) for nested_lst in lst]

print(sorted_lst)