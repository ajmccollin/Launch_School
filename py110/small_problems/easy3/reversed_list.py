'''
P - Create a function that takes a list as an argument and reverse the elements
        without using a slice or list.reverse method. 
E -  E: Cannot use the reverse method or a list slice.
        Output list should be mutated and should be same as the argument.
        
    IQ:
D -  I:
     O:
     N:
A -
'''
# FIRST APPROACH, STILL FUNCTIONAL
# def reverse_list(input_list):
#     count = len(input_list)
#     while count > 0:
#         input_list.append(input_list.pop(count - 1))
#         count -= 1
#     return input_list

def reverse_list(input_list):
    first = 0
    last = -1

    while first < (len(input_list) // 2):
        input_list[first], input_list[last] = input_list[last], input_list[first]
        first += 1
        last -= 1

    return input_list

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True