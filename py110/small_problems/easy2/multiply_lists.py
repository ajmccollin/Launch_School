def multiply(num1, num2):
    return num1 * num2

def multiply_list(list1, list2):
    return [multiply(num1, num2) for num1, num2 in zip(list1, list2)]
    

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True