def triangle(number):
    for num in range(1, number + 1):
        print((' ' * (number - num)), '*' * num)

triangle(5)
triangle(9)