def sort_by_consonant_count(strings):
    strings.sort(key=consecutive_consonant_count, reverse=True)
    return strings


def consecutive_consonant_count(string):
    joined_string = ''.join(string.split(' '))
    character_count = 0
    adjacent_consonant = ''
    vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
    for letter in joined_string:
        if letter not in vowels:
            adjacent_consonant += letter
            if (len(adjacent_consonant) > character_count and 
            len(adjacent_consonant) > 1):
                character_count = len(adjacent_consonant)
            adjacent_consonant = ''
        elif letter in vowels:
            if (len(adjacent_consonant) > character_count and 
            len(adjacent_consonant) > 1):
                character_count = len(adjacent_consonant)
            adjacent_consonant = ''
    return character_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list)) # ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list)) # ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list)) # ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list)) # ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list)) # ['xxxx', 'xxxb', 'xxxa']