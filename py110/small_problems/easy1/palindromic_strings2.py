def is_real_palindrome(input_string):
    s = ''
    for char in input_string:
        if char.isalnum() == True:
            s += char.lower()
    return s == s[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True
print(is_real_palindrome('Madam') == True)           # True
print(is_real_palindrome("Madam, I'm Adam") == True) # True