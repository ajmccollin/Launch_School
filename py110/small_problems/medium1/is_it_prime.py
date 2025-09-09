'''
P - Define a function that takes an integer and returns True if the number is
    prime, False otherwise. 
E - E: Prime numbers are only divisible by 1 and itself.
       1 is not considered prime
       Cannot use any python modules or packages.
    I: A valid integer will always be passed as the argument.
D - I: An integer
    O: A boolean value.
    N: Iterate over the range from 2 to the passed integer minus 1.
        For each number in the range, if the quotient of the  passed integer 
            divided by that number is an integer, return True
        is_instance(quotient, int)?
A - 1. Define a function called `is_prime` with the parameter `input_integer`
    2. Set guard clauses
        3. If the argument is 0, return False
           If the argument is 2, return True
           Otherwise, continue in the function.
    4. Iterate over the integeres in range from 2 to the input_integer.
        If the quotient of the input_integer divided (float division) by the 
        iteration number is an integer, return False.
    5. Otherwise return True. 
'''
def is_prime(input_integer):
    if input_integer == 1:
        return False
    
    for num in range(2, input_integer):
        if input_integer % num == 0:
            return False
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True