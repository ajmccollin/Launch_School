import pprint

statement = "The Flintstones Rock"
joined_string = ''.join((statement.split()))
char_count = {}

for idx, char in enumerate(joined_string):
    if joined_string[idx] not in char_count:
        char_count[char] = 1
    elif joined_string[idx] in char_count:
        char_count[char] += 1
        
# LS Solution
# char_freq = {}
# statement = statement.replace(' ', '')
# for char in statement:
#     char_freq[char] = char_freq.get(char, 0) + 1

# print(char_freq)

pprint.pprint(char_count)