def running_total(my_list):
    new_list = []
    if len(my_list) <= 1:
        return my_list
    else:
        starting_number = my_list[0]
        new_list.append(starting_number)
        index = 1

        while index < len(my_list):
            previous_element = new_list[index - 1]
            new_list.append(previous_element + my_list[index])
            index += 1
        return new_list
    
#LS Solution/ Simplified Solution
#def running_total(nums):
    # result_list = []
    # total = 0

    # for num in nums:
    #     total += num
    #     result_list.append(total)

    # return result_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
       == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
            




