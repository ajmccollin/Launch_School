def lengthy_upper_case(input_string):
    if len(input_string) > 10:
        return input_string.upper()
    else:
        return user_string

user_string = input('Please enter a string: ')
print(lengthy_upper_case(user_string))