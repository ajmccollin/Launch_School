#ask user for age
#ask user what age they would like to retire at
#state the date, and the date + retirement age
    #import date_time module to get correct date
#return future_date - current_date
import datetime

year = datetime.datetime.now().year

user_age = int(input('What is your current age? '))
retirement_age = int(input('At what age would you like to retire? '))
retirement_year = year + (retirement_age - user_age)

print(f'It\'s {year}. You will retire in {retirement_year}')
print(f'You have only {retirement_year - year} years of work to go!')