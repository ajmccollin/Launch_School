'''
P - Define a function that takes a string as an argument and returns a string 
    where the characteres alternate between capitalized and non-capitalized.
E - E:  Alternate between capitalized and non-capitalized. 
        Non- alphabetical characters don't get change, but count as characters.
    I:  The string can contain any character.
        Start the alternation with the first character being capitalized.
    Q: Spaces? Do they count?
D - I: String
    O: A new string where the 
    N: Even/Odd index
        .isalpha method
A - 1. Define a function called `staggered_case` that sets `input_string`
        as the parameter.
    2. Create an empty string
    3. Iterate over each character of the string, setting the idx and char, 
        calling the enumerate function on the input_string.
    4. If the index is odd, append the uppercase character to the empty string
    5. If the index is even, append the uppercase character to the empty string.
    6. For both conditionals, only append the chacter if it is alphabetical, if
        not, append the character directly.
    7. return the final string.
'''
def staggered_case(input_string):
    staggered_string = ''

    for idx, char in enumerate(input_string):
        if idx % 2 == 0: # Even indices, starting at idx 0
            staggered_string += char.upper()
        else: # Odd indices, startings at 1
            staggered_string += char.lower()
            
    return staggered_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True