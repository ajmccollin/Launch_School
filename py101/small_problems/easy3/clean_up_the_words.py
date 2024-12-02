#Define a function that returns a string with all non-alphabetic characters
    #replaced by spaces
#There should only be one space in a row at a time


def clean_up(string):
    cleaned_up = ''
    for inx, char in enumerate(string):
        if char.isalpha():
            cleaned_up += char
        elif inx == 0 or cleaned_up[-1] != ' ':
            cleaned_up += ' '
    return cleaned_up

            

print(clean_up("---what's my +*& line?") == " what s my line ") #True
print(clean_up("---what's my +*& line?"))