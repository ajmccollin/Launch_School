#def a function that:
    #returns the next to last word in str 
    #any non_blank sequence of characters
    #input will always contain at least two words

def penultimate(string):
    string_list = string.split()
    return string_list[-2]

# These examples should print True

print(penultimate("last word"))
print(penultimate("Launch School is great!"))

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")