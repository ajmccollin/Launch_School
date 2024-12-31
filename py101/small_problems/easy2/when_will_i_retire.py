from datetime import datetime

user_age = int(input("What's your age? "))
retirement_age = int(input("At what age would you like to retire? "))
years_to_retirement = retirement_age - user_age

current_year = datetime.now().year
retirement_year = current_year + years_to_retirement
print(f"It's {current_year}. You will retire in {retirement_year}")
print(f"You only have {years_to_retirement} years of work to go! ")


