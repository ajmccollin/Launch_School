def is_palindrome(input_string):
    half_length = len(input_string) // 2
    if len(input_string) % 2 == 0: # length is even
        first_half = input_string[0: half_length]
        second_half = input_string[len(input_string): half_length -1 : -1]
        return first_half == second_half
    elif len(input_string) % 2 == 1: # length is odd
        first_half = input_string[0: half_length + 1]
        second_half = (input_string[len(input_string): half_length - 1 : -1])
        return first_half == second_half

# Or the much simplier function...
# def is_palindrome(s):
#    return s == s[::-1]

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
print(is_palindrome('Madam') == False)
print(is_palindrome("madam i'm adam") == False)