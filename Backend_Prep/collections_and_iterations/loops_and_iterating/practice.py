#my_list = [6, 3, 0, 11, 20, 4, 17]

'''
counter = 0
while counter < len(my_list):
    print(my_list[counter])
    counter +=1
'''

'''
for num in my_list:
    print(num)
'''

'''counter = 0
while counter < len(my_list):
    if my_list[counter] % 2 == 0: 
        print(my_list[counter])
    counter += 1
'''
'''
for num in my_list:
    if num % 2 == 1:
        print(num)
'''

'''
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
'''

'''
for nested in my_list:
    for num in nested:
        if num % 2 == 0:
            print(num)
'''

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

numbers = []
for num in my_list:
    if num % 2 == 1:
        numbers.append('odd')
    else:
        numbers.append('even')
print(numbers)