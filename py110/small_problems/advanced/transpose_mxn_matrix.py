'''
P - Create a function that switches columns and rows for a passed in matrix.
E -  E: Rows and Columns might not be equal.
        The function should swap the rows to columns and vice versa.
        There will be at least one row and one columnn. 
    IQ: The output should flip the number of rows and the number of columns
        May or may not want to use function(s) from previous exercise.
D -  I: A MxN matrix where the number of rows and column may or may not match.
     O: A matrix with rows and columns flipped.
     N: will need to use the len function and iteration. 
        Will most likely need to use indices.
A - 1. Change tranpose function but keep transpose once function.
    2. Chenge tranpose function so it repeats for as many times as the len of 
'''

def transpose_once(matrix, idx):
    return [row[idx] for row in matrix]

def transpose(matrix):
    return [transpose_once(matrix, num) for num in range(len((matrix)))]



# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) ) #== [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]])) # == [[1, 2, 3, 4]])
print(transpose([[1]])) # == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)