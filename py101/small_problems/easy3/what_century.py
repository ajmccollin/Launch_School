#define a function that:
    #takes year as input and returns the century
    #remove last 2 digits if greater than 100
        #if less than 100, return 1st century
    #appropriate suffix (ex: 'st', 'nd', 'rd', 'th', etc.)

def century(year):
    if year < 100:
        return "1st"
    else:
        century = (year // 100) + 1
        if year % 100 == 0:
            century -= 1
        last_two_digits = century % 100
        last_digit = century % 10

        match last_two_digits:
            case 11 | 12 | 13:
                return (f'{century}th')
            
        match last_digit:
            case 1:
                return (f'{century}st')
            case 2:
                return (f'{century}nd')
            case 3:
                return (f'{century}rd')
            case _:
                return (f'{century}th')


print(century(2000))
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True