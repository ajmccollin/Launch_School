'''
P - Create a function that returns a list of substrings only if the substring
    is palindromic.
E - I: string
    O: List of potential palindromic strings (or an empty list)
    E: if sustring does not contain any palindromes, then returns empty list
        - dupes should be inlcluded
        - should use substring function from previous exercise
        - capitalization and punctuation are important.
    I: Input will always be valid.
D - List of substrings.
A - 1. Paste function from previous exercise.
    2. Set conditon that the string should only be appended if it is the same
        forwards as backwards.
    3. return list of palindromic substrings.
'''

def leading_substrings(input_str):
    return [input_str[0: idx] for idx in range(1, len(input_str) + 1)]

def substrings(input_str):
    list_of_lists = [leading_substrings(input_str[idx:]) 
            for idx in range(len(input_str))]
    return [item for sublist in list_of_lists for item in sublist]

def palindromes(input_str):
    return [substring for substring in substrings(input_str) 
            if (substring[::-1] == substring) and len(substring) > 1]
        
        

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True