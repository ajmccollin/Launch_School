def word_sizes(string):
    word_count = {}
    new_string = ''

    for char in string:
        if char.isalnum() or char.isspace():
            new_string += char
    split_string = new_string.split()
    
    for word in split_string:
        word_count.setdefault(len(word), 0)
        word_count[len(word)] += 1

    return word_count

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})