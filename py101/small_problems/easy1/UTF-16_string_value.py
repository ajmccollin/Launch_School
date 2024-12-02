def utf16_value(string):
    index = 0
    collection = []
    while index < len(string):
        collection.append(ord(string[index]))
        index += 1
    return sum(collection)


'''
def utf16_value(string):
    total_sum = 0
    for char in string:
        total_sum += ord(char)
    return total_sum
'''

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)