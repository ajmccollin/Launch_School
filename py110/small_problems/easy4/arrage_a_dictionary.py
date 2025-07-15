def get_value(my_dict):
    return my_dict[1]

def order_by_value(my_dict):
    sorted_dict = sorted(my_dict.items(), key=get_value)
    return [key for key, value in sorted_dict]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True