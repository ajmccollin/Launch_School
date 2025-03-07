def crunch(string):
    new_string = ''
    prev_char = ''
    for char in string:
        if char != prev_char:
            new_string += char
            prev_char = char
    return new_string

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('ddaailly'))
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')