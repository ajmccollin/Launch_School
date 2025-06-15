def interleave(list1, list2):
    combined_lst = [item for pair in zip(list1, list2) for item in pair]
    return combined_lst



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
