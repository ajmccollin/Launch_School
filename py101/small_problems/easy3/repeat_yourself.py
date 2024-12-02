#function that takes two arguements
    #string and positive number
#print string for as many times as the number indictated

def repeat(string, num):
    count = 0
    while count < num:
        print(string)
        count += 1
    
repeat('Hello', 3)