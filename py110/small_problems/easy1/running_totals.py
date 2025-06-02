def running_total(user_list):
    running_sum = []
    running_count = 0

    for num in user_list:
        running_count += num
        running_sum.append(running_count)
        
    return running_sum

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True