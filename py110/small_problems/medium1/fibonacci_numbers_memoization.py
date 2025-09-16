'''
P - Utilizing the fibonacci function from the prevous exercise, modify the 
        function so it stores the values into a dicitonary and checks to see if
        the value is in the dictionary before fully calculating the next fib.
E -  E: Store the values in a collection that way the values do not need to be
            calculated each time. 
    IQ: 
D -  I:
     O:
     N: Store values in a dict
        Create a conditional to check whether the value is in the dict, if not  
            create a key/value item for that specific pair.
A - Create a dictionary where the integers 1 and 2 are assigned as keys to the 
        values 1 and 1.
    Alter the function so if nth is in dictionary, return that value.
        If it is not, create that key/value pair.
'''
# More incapulated without side effects, non-globally stored variables
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
    
# fibonacci_sequence = {}
# def fibonacci(nth):
#     if nth <= 2:
#         return 1

#     if nth in fibonacci_sequence:
#         return fibonacci_sequence[nth]

#     fibonacci_sequence[nth] = (fibonacci(nth -1 ) + fibonacci(nth - 2))
#     return fibonacci_sequence[nth]



print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True