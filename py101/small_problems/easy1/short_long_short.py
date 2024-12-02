#Def a function that: 
    #Takes two strings as argument
    #Determines legnth of string
    #Returns concatenation of shorter string, longer string, shorter string

def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")