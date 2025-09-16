'''
P - Create a function that takes a year as an argument and returns how many 
        days in that year fall on friday the 13th. 
E -  E: The year is greater than 1752 thich is the gregorian calendar.
        The input is an integer that represents the year.
    IQ: Use the datetime.time import module.
        Can be any date in the foreseeable future.
D -  I: An integer representing a year
     O: An integer that shows the number of Friday the 13ths in that year.
     N: Might want to use the datetime.time module.
        Have a separate count that increases when Friday 13th is True
        Maybe use a dictionary? Or zip up dict pairs somehow and .get method.
A -  Create a function that takes an integer year as the argument. 
     Create a variable called `count` that is equal to 0.
     Iterate over each month in the given year.
     Create a conditional that if the 13th falls on a friday of that year, 
        increase count. 
     Return that count. 
'''
import datetime

def friday_the_13ths(input_year):


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True