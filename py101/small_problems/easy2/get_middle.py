def center_of(message):
    half_length = len(message) // 2
    if len(message) % 2 == 1: #Odd length
        return message[half_length]
    else:
        return message[half_length - 1: half_length + 1] #Even length

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True