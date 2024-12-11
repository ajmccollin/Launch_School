def add(left, right):
    sum = left + right
    return sum

num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

sum = add(num1, num2)
print('The sum of your numbers is ' + str(sum))