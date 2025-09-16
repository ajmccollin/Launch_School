'''
P -  Create a function that takes a nested list of lists and returns 
E -  E: Return a transposed matrix, 
    IQ: Need to double access the list. list[0][0]
        The argument will always be a valid matrix. 
D -  I: Matrix, a list of lists.
     E: Another matrix, but transposed.
     N: Iterate over each list in the nested list and append specific
            index to new list. 
        For list in list, return list[0]?
        While count < len(matrix):
            iterate over each list, count += 1
A -  1. Create a function called tranpose that takes `matrix` as the argument.
     2. Set a value `count` equal to 0.
     3. Create a conditional that execute until count is greater than length of
            matrix.
     4. Iterate over each list in matrix, returning the list at 0 and storing
            into a list.
     5. Increate count by one and repeat.
     6. Return the new transposed list.
'''
def transpose_once(matrix, idx):
    return [row[idx] for row in matrix]

def transpose(matrix):
    return [transpose_once(matrix, num) for num in range(len((matrix)))]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix== [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True