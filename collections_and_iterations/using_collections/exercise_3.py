my_tuple = (1, 2, 3, 4, 5)

my_tuple = list(reversed(my_tuple))
my_tuple.remove(1)
my_tuple.remove(5)

print(tuple(my_tuple))


my_second_tuple = (1, 2, 3, 4, 5)
result = my_second_tuple[-2: -5: -1]
print(result)