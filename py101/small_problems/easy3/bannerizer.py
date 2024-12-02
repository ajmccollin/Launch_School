def print_in_box(string):
    length = int(len(string))
    
    print('+-' + ('-' * length) + '-+')
    print('|', (' ' * length), '|')
    print('|', f'{string}', '|')
    print('|', (' ' * length), '|')
    print('+-' + ('-' * length) + '-+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')