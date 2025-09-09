'''
P - Create a function that determines the next featured number. 
E -  E: A featured number meets the following requirements:
            1. divisible by 7
            2. odd
            3. no repeated numbers.
        If there is not another featured number, return 'There is no possible 
            number that fulfills those requirements.'
     IQ:Input always valid?
D -  I: integer
     O: An integer that is the next featured number (meets requirements)
     N: Exception handling: if num > 9876543200 #greatest featured num, return 
            phrase.
        While loop?
A - 1. Create 3 functions
        a. Determines if the number is odd
        b. determines if the number is divisible by 7
        c. deterimines if the number contains no repeated integers.
    2. Create a loop that add 1 to the number until is_odd and divisible by 7
        is true. 
    3. If it is also not a repeated integer, return that number, otherwise, add
        14 until it meets are 3 function requirements.
'''
ERROR_MESSAGE = 'There is no possible number that fulfills those requirements.'
LARGEST_FEATURED_NUM = 9876543201

def is_odd(num):
    return num % 2 == 1

def divisible_by_7(num):
    return num % 7 == 0

def unique_digits(num):
    return len(str(num)) == len(set(str(num)))

def next_featured(num):
    next_featured = num + 1
    if next_featured > LARGEST_FEATURED_NUM:
        return ERROR_MESSAGE
    
    while not all((is_odd(next_featured), divisible_by_7(next_featured))):
        next_featured += 1

    while not all((is_odd(next_featured), divisible_by_7(next_featured), 
                   unique_digits(next_featured))):
            next_featured += 14
            if next_featured > LARGEST_FEATURED_NUM:
                 return ERROR_MESSAGE

    return next_featured

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True