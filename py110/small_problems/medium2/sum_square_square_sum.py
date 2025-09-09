'''
P - Create a function that calculates the difference between the sum of `count`
        numbers minus the sum of the square of `count` numbers.

E - E:  The argument `count` is being passed.
        Calculate the sum from 1 to count + 1, then square.
        Subtract the sum of the square of each number from 1 to count + 1.
    IQ: Will the numbers always be positive integers?
        Do not include 0, since it needs to be positive integers.
        Include the `count` argument, so count + 1
D - I:  Integer
    O:  Integer which is the difference of the sum_square and square_sum.
    N:  Might want to use two different functions, one to determine the square 
        of the sums and one to determine the sum of sqaures.
A - 1. Create a function called sum_squared that takes an integer as the argument.
        a. Iterate over each number in range from 1 to the passed integer.
        b. Find the sum of the numbers in range and square the total.

    2. Create a function called squared_sum that takes an integer as the argument.
        a. Iterate over each number in the range and return the number squared.
            using a list comprehension and store as squared_num. 
        b. return the sum of the list.
    
    3. Create a function called sum_square_difference that takes an integer as
        the argument. 
            a. Call sum_squared and subtract squared_sum and return the difference.
'''
def sum_squared(num):
    total_sum = sum(range(1, num + 1))
    return (total_sum**2)

def squared_sum(num):
    return sum(num**2 for num in range(1, num + 1))

def sum_square_difference(num):
    return sum_squared(num) - squared_sum(num)

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True