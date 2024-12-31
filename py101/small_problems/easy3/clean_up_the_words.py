def clean_up(message):
    new_message = ''
    for char in message:
        if char.isalpha():
            new_message += char
        elif not new_message.endswith(' '):
                new_message += ' '
                
    return new_message



print(clean_up("---what's my +*& line?") == " what s my line ") #True
print(clean_up("---what's my +*& line?"))
print(clean_up(''))
print(clean_up('') == (''))