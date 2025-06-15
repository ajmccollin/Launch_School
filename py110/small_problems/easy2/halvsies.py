def halvsies(lst):
    half_length = len(lst) // 2
    if len(lst) % 2 == 1:
        first_half = lst[0: half_length + 1]
        second_half = lst[half_length + 1: ]
    else:
        first_half = lst[0: half_length]
        second_half = lst[half_length: ]

    return [first_half, second_half]    

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])