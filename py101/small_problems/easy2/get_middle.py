def center_of(string):
    if len(string) % 2 == 1: #Odd case
        return string[len(string) // 2]
    elif len(string) % 2 == 0: #Even case
        right_case = string[len(string) // 2]
        left_case = string[(len(string) // 2) - 1]
        return left_case + right_case
    else:
        print('This is an empty string! ')

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True