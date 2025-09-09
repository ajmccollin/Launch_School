'''
P -  Modify the previous function to exclude non-letter characters.
E -  E: Only count letters, but each word is still considered one word even if
            there are non_letters in the string. 
     IQ: Only letters, so no non-ASCII char, numbers, or punct.
D -  I: A string
     O: A dictionary where the key is the len of the str and the value is the
            number of occurrences for that string's length.
     N: Might want to create a separate function to determine letter count?
            If char .isalpha, count + 1 or something?
A - 1. Create a function called char_count that takes one str argument.
    2. Create a variable called letter_count equal to 0
    3. For each char in input_word, if the character is a letter, increase 
        letter_count by 1.
    4. return letter_count.

    1. Using the previous function, in the for loop, create a variable called
            true_length and set that equal to calling the char_count function
            on the word. 
    2. Then change the `len(word) strictly to the true_length variable.
'''
def number_of_letters(word):
    count = 0

    for char in word:
        if char.isalpha():
            count += 1
    
    return count

def word_sizes(input_str):
    word_sizes = {}
    split_string = input_str.split()

    for word in split_string:
        letter_count = number_of_letters(word)
        if letter_count > 0:
            word_sizes[letter_count] = word_sizes.get(letter_count, 0) + 1
    
    return word_sizes

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})