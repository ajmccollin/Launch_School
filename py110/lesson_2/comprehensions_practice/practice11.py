'''
The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) that appears 
in the contained strings, then print it.
'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = {'a', 'e', 'i', 'o', 'u'}
# list_of_vowels = []
# for nested_lst in dict1.values():
#     for strings in nested_lst:
#         [list_of_vowels.append(char) for char in strings if char in vowels]

vowel_check = [char for key in dict1
               for lst in dict1[key]
               for word in lst 
               for char in word if char in vowels]

print(vowel_check)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
