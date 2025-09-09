'''
P - Create a function that takes a string and replaces every occurence of
    a number word with it's cooresponding number.
E - E: There is no punctuation.
       'zero' - 0
       'one' - 1
       'two' -2 ... etc. (up to 9)
    I/Q: Does capitalization matter? 
D - I: A string
    O: A string with number words converted to numbers. 
    N: a dictionary might be useful
       split method and iteration over split words? then join?
A - 1. Define a function called `word_to_digit` with the parameter `input_str`
    2. Create a dictionary with the number word as the key and the number as 
        the value.
    3. Split the string and iterate over each word.
    4. If the word is a key in the dictionary, replace that word with the 
        dictionary value cooresponding.
    5. Return the joined list. 
'''
WORDS_TO_NUMBERS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def word_to_digit(input_str):
    word = input_str.split()
    output_lst = [WORDS_TO_NUMBERS.get(word, word) for word in word]
    return ' '.join(output_lst)


message = 'Please call me at five five five one two three four'
print(word_to_digit(message))# == "Please call me at 5 5 5 1 2 3 4")
# Should print True