# Input: String
# Output: Dictionary with key being len of string, value being the occurences 
#   of that string


# Explicit: There can be zero words 
# Implicit: Punctuation does not count as a space and will count in the len of a string

# Other Questions:
# Are multiple spaces considered strings or should they be spilt

# Examples: All should print True
    # string = 'Four score and seven.'
    # print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

    # string = 'Hey diddle diddle, the cat and the fiddle!'
    # print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

    # string = 'Humpty Dumpty sat on a wall'
    # print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

    # string = "What's up doc?"
    # print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

    # print(word_sizes('') == {})
        #Empty Strings create empty dictionaries

# Data Types:
#   Dictionary

# Algorithm
#   1. Create an empty dictionary 'word_count'
#   2. Split the string by whitespace and assign to 'split_string'
#   3. Iterate over each word in the 'split_string'
#   4. Create a dictionary item with len of string being the key and increase
#       the value by 1
#   5. If the key already exists, increment the value by one
#   6. Return the dictionary

def word_sizes(string):
    split_string = string.split()
    word_count = {}

    for word in split_string:
        word_count.setdefault(len(word), 0)
        word_count[len(word)] += 1

    return word_count



string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})