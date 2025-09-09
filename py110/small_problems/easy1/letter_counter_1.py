'''
P - Create a function that takes a string and counts the occurrences of each   
        len of string.
E - E: - Words are split at non-space characters.
       - strings are separated by zero or more spaces
       - Output is a dictionary consisting of len(word): len occurrences
       - Empty strings return empty dictionaries.
    I: Input will be valid.
D - I: String
    O: Dictionary
    N: Will probably need to use default = 0 or .get method
       Will need to split words and store in a new list.
A - 1. Define a function called word_sizes that takes the parameter input_string
    2. Split the input_string and store into a list
    3. Iterate over each string in the list, creating a dictionary item for 
            the len of the string and the count, or adding 1 if it exists.
    4. Return the dictionary.
'''
def word_sizes(input_str):
    word_sizes = {}
    split_string = input_str.split()

    for word in split_string:
        word_sizes.setdefault(len(word), 0)
        word_sizes[len(word)] += 1
    
    return word_sizes

# All of these examples should print True
string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})