'''
P - Create a function that takes a string and returns every string in a list
        followed by a space and the length of the string.
E - E:  - Every pair of words is separated by a space.
        - dupes are repeated
        - return object is a list of strings, a space, and a number.
    I:
    Q:  - Double whitespace returns?
D - I: String
    O: List of strings.
    T: Use len/split functions?
A - 1. Create a function called word_lengths that takes the parameter words. 
    2. Split words into a list called word_list
    3. Create a new empty list called expected result.
    4. Iterate over each string in the list, determining the string length and
        using the += operator to add a whitespace and len. s
    5. Add new values to expected_list
    6. Return results. 
'''
def word_lengths(words=''):
        return [(f"{word} {len(word)}") for word in words.split()]

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True