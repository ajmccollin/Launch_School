'''
P - Define a function that takes a string as an argument and swaps the first
        and last letter of every word. 
E -  E: The string contains only words and spaces, all words only contain letters
        There are no leading, repeated or trailing spaces. -> split()
        Every word is at least 1 letter long => dont need to worry about empty
            strings.
     IQ: The argument will always be valid.
         Single letters return single letters. 'a' returns 'a'
D -  I: String
     O: A new string with the first and last letters of each string swapped.
     N: .split()
        might want to create a helper function that swaps first and last
A - 1. Create a fucntion called word_swap that takes `input_str` as an argument.
    2. return input string from -1 to 1:len(string) to index 0.

    1. Create a function called swap that takes one string as the argument.
    2. Initialize a variable called `swapped_words` that is assigned to an empty
        string.
    3. For each word in the input string, call the word_swap function and 
        concatenate that output with swapped_words. 
    4. return swapped words.
'''
def letter_swap(word):
    if len(word) > 1:
        swapped_word = f"{word[-1]}{word[1: -1]}{word[0]}"
        return swapped_word
    return word

def swap(input_str):
    swapped_lst = [letter_swap(word) for word in input_str.split()]
    return ' '.join(swapped_lst)

print(swap('Oh what a wonderful day it is') 
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True