def penultimate(message):
    split_words = message.split()
    return split_words[-2]

print(penultimate("last word"))
print(penultimate("Launch School is great!"))

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")