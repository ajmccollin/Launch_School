def is_exclamation(string):
    if string.endswith('!'):
        print('True')
    else:
        print('False')

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

is_exclamation(str1)
is_exclamation(str2)

print(str1.endswith('!'))
print(str2.endswith('!'))