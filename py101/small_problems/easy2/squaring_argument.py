#using multiply function from previous problem:
    #write a funciton that computes square of it's argument
def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)
        
print(square(5) == 25)   # True
print(square(-8) == 64)  # True
