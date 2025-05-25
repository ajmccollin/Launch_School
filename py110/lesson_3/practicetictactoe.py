'''
Problem:
    I: A range, delimiter, connector
	O: A range of number connected by the delimiter, ending with the connector.
	
Example Cases:
    print(join_or([1, 2, 3]))               # => "1, 2, or 3"
    print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
    print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
    print(join_or([]))                      # => ""
    print(join_or([5]))                     # => "5"
    print(join_or([1, 2]))                  # => "1 or 2"
	
Data Types:
    Input: List of integers and two strings
	Return one string
	
Algorithm:
    X 1. Define function that takes 3 inputs (range, delimiter, connector. 
    2. Iterate over each element in the range up until the last item. 
	    Return that item followed by the delimiter.
    3. For the last item, return the connector followed by the last item in range. 
    X 4. If the length of the list is less than or equal to 1, return the list. 
    X 5. Set default delimiter to a blank space and default connector to "or"
'''

def join_or(num_range, delimiter=', ', connector='or'):
    match len(num_range):
        case 0:
            return ''
        case 1:
            return str(num_range)
        case 2:
            return f"{num_range[0]} {connector} {num_range[1]}"
    
    starting_nums = delimiter.join(str(num) for num in num_range[0: -1])
    return f'{starting_nums} {connector} {num_range[-1]}'

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"