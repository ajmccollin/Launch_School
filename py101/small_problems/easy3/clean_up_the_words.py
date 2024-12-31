def clean_up(message):
    for char in message:
        if char.isalpha():


print(clean_up("---what's my +*& line?") == " what s my line ") #True
print(clean_up("---what's my +*& line?"))