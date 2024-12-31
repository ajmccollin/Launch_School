#write a function that:
    #takes a positive int
    #returns a string of alternating 1 and 0 starting with 1
def stringy(int_value):
    string_value = ''
    for num in range(1, int_value + 1):
        added_number = '1' if num % 2 == 1 else '0'
        string_value += added_number
    return string_value


print(stringy(6))
print(stringy(4))
print(stringy(7))

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True