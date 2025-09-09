'''
P -  Modify the function from the previous exercise so that only letters are
        counted when swapping the case. Non-alphabetical characters do not
        count towards the count. 
E -  E: Ignore non_alphabetical chars. 
    IQ:
D -  I: String
     O: String which alternates the casing for letters only.
     N: Add a count, if even, upper(), if odd, lower()? add count if alpha()
A -  
'''

def staggered_case(input_string):
    staggered_string = ''
    count = 0

    for char in input_string:
        if count % 2 == 0 and char.isalpha(): # Even indices, starting at idx 0
            staggered_string += char.upper()
            count += 1
        elif count % 2 == 1 and char.isalpha(): # Odd indices, startings at 1
            staggered_string += char.lower()
            count += 1
        else:
            staggered_string += char
            
    return staggered_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True