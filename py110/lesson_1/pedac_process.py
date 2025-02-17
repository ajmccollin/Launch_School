# 1. Create a empty ‘rows’ list to hold all of our rows
# 2. Create a ‘row’ list and add it to the overall ‘rows’ array/list
# 3. Repeat step 2 until all the necessary rows have been created
#   - All the rows have been created when the length of the ‘rows’ list is equal to the input. 
# 4. Sum the final row 
#   - Add all integers in the row
# 5. Return the sum


def sum_even_number_row(row_number):
    rows = []
    start_integer = 2
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = row[-1] + 2
    return sum(rows[-1])

def create_row(start_integer, row_length):
    row = []
    current_integer = start_integer
    while len(row) < row_length:
        row.append(current_integer)
        current_integer += 2
    return row

print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

print(create_row(2, 1) == [2])
print(create_row(4, 2) == [4, 6])
print(create_row(8, 3) == [8, 10, 12])
