def reverse_string(string):
    for char in string:
        string = char + string
    return string

print(reverse_string("hello")) # == "olleh")