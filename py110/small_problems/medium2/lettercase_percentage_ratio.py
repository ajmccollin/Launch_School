'''
P - Create a function that creates a dictionary that shows the percentage of 
        lowercase chracters, uppercase characters, and neither from a string.
E - E: The output is a dictionary with the keys `lowercase`, `uppercase`, and 
            `neither`.
        Each percentage is stored as a string and rounded to 2 decimals.
        Always at least one character in a string. 
    I/Q: What do non ASCII characters fall under? ex: ß or double ss?
         Solve without using any python inputs? or is the math module allowed?
D - I: A string with heterogenous mixture of upper and lower chars and neither.
    O: A dictionary containing three keys, `uppercase`, `lowercase` and `neither`
        with the values being the percentage repectively.
    N: Have a count that adds one if it is caps, otherwise add to a diff var.
       Divide one count by the sum to get the percentage? 
       XX:2f
A - 1. Define a function called letter_percentages with the parameter `input_str`
    2. Create a dictionary called percentage_dict.
        a. Either create the three needed keys here, or use the .get method 
            to later add them.
    3. Create three variables, upper_count, lower_count, and neither_count all
            assigned to the integer 0.
    4. Iterate over each char in the string
        a. If the character is lowercase, add 1 to lower_count.
        b. If the character is uppercase, add 1 to upper_count. 
        b. If neither, add 1 to neither_count.
    5. Assign the value of lower_count divided by length of input string to
        lowercase. Repeate for upper and neither.
    6. Return the dictionary.
'''
def calculate_percentage(count, total):
    return f"{count / total * 100:.2f}"

def letter_percentages(input_str):
    percentage_dict = {}

    lower_count = 0
    upper_count = 0
    neither_count = 0
    total = len(input_str)

    for char in input_str:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            neither_count += 1
    
    percentage_dict['lowercase'] = calculate_percentage(lower_count, total)
    percentage_dict['uppercase'] = calculate_percentage(upper_count, total)
    percentage_dict['neither'] = calculate_percentage(neither_count, total)
    
    return percentage_dict
    ''' Can also return the function without storing it in a variable:
    return {
    'lowercase': calculate_percentage(lower_count, total),
    'uppercase': calculate_percentage(upper_count, total),
    'neither': calculate_percentage(neither_count, total),
    } 
    '''

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)