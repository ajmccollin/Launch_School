def factors(number):
    divisor = number
    result = []
    while (divisor != 0):
        if number < 0:
            result = 'Please enter a number greater than 0'
            break
        elif number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(int(input())))