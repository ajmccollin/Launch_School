'''
P - Create a function that determines which fibonacci number has the specified
        number of digits as the passed in integer argument. 
E -  E: Need to import sys module in order to access greater number length.
        Length of the fib numbers needs to equal the passed through int. 
        Argument is greater than or equal to 2
    IQ: Will the passed through argument always be an integer?
D -  I: Ingeter representing the legnth needed.
     O: The integer representing the fibonacci number (iterations) needed to 
            meeted input argument.
     N: Convert to string and calculate length?
A - Import the sys module
    Copy function from previous exercise.
    Define a new function called `find_fibonacci_index_by_length` that takes a
        single integer as the argument.
    Create a variable named `count` that is assigned to the integer 2.
    Create a loop that calls the fibonacci function with the argument count and 
        iterates until the len of the value (calling the str on the int) is 
        equal to the passed in argument integer.
        else: count +1
    Return count
'''
import sys

sys.set_int_max_str_digits(50_000)

def fibonacci(nth, fibonacci_sequence = None):
    if fibonacci_sequence == None:
        fibonacci_sequence = {}
        
    if nth <= 2:
        return 1
    elif nth in fibonacci_sequence:
        return fibonacci_sequence[nth]
    else:
        fibonacci_sequence[nth] = (fibonacci((nth - 1), fibonacci_sequence) + 
                                   fibonacci((nth - 2), fibonacci_sequence))
        return fibonacci_sequence[nth]
    
def find_fibonacci_index_by_length(integer):
    count = 1 
    fibonacci_sequence = {}
    while len(str(fibonacci(count, fibonacci_sequence))) < integer:
        count += 1
    return count

    

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)