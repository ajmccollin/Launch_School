def crunch(user_string):
        new_string = ''

        for idx, char in enumerate(user_string):
            if char != user_string[idx - 1]:
                new_string += char
        return new_string
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('ggggggggggggggg'))
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
