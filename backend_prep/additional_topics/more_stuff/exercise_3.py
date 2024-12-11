import math as m

def sum_of_sqaures(num1, num2):
    def square(num):
        return num * num
    return square(num1) + square(num2)

print(sum_of_sqaures(3, 4))
print(sum_of_sqaures(5, 12))