def multiply_list(lst):
    doubled_list = []
    for item in lst:
        doubled_list.append(item * 2)

    return doubled_list

print(multiply_list([1, 2, 3])) # == [2, 4, 6])