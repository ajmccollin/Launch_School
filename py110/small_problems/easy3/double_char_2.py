VOWELS = ('a', 'e', 'i', 'o', 'u')

def double_consonants(string):
    duplicated_string = ''

    for char in string:
        if char.isalpha() and char.lower() not in VOWELS:
            duplicated_string += char * 2
        else:
            duplicated_string += char

    return duplicated_string
            

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")