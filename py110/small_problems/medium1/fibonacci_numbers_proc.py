'''
P - Create a function that computes the nth Fibonacci number.
E - E:  A fibonacci number is the sum of the two previous numbers in a sequence,
            starting at 0 + 1, 1 + 1, 1 + 2, 2 + 3, etc...
        Start with the first two numbers equal 1, 
    I/Q: What if 0 is passed as an integer?
D - I: An integer, which represents the nth fibonacci number.
    O: The sum of the fibonacci numbers, represented as an integer.
    N: Use the range function?
A - 1. Define a function called fibonacci with the parameter nth_num
    2. Create a conditional, if nth is less than 2, return 1.
    3. Create two variables, previous and current and set both equal to 1.
    4. iterate over each number in range of 3, nth number.
        for each iteration, set previous equal to current and current equal to 
                previous plus current.
        return current. 
'''
def fibonacci(nth):
    if nth <= 2:
        return 1
    
    previous = 1
    current = 1

    for _ in range(3, nth + 1):
        previous, current = current, current + previous

    return current

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True