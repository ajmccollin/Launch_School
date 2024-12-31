def crunch(user_string):
    if len(user_string) > 0:
        new_string = user_string[0]
        index = 0
    else:
        return user_string

    for char in user_string:
        if char == new_string[index]:
            continue
        new_string += char
        index += 1
    return new_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
