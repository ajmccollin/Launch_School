def is_balanced(string):
    parenthesis_list = [char for char in string if char == ')' or char == '(']
    cleaned_string = "".join(parenthesis_list)
    while "()" in cleaned_string:
        cleaned_string = cleaned_string.replace("()", "")
    return len(cleaned_string) == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True