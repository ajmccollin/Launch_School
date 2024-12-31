def print_in_box(user_input):
    str_length = int(len(user_input))
    banner_header = ('+-' + '-' * str_length + '-+')
    empty_borders = ('| ' + ' ' * str_length + ' |')
    text_line = ('| ' + user_input + ' |')
    print(banner_header)
    print(empty_borders)
    print(text_line)
    print(empty_borders)
    print(banner_header)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')