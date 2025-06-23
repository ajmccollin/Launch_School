MINUTES_PER_HOURS = 60
HOURS_PER_DAY = 24

def time_of_day(num):
    if num >= 0:
        hours = num // MINUTES_PER_HOURS
        while hours > HOURS_PER_DAY:
            hours -= HOURS_PER_DAY

        minutes = num % MINUTES_PER_HOURS
    else:
        hours = 23 - (-(num) // MINUTES_PER_HOURS)
        while hours < 0:
            hours += HOURS_PER_DAY

        minutes = MINUTES_PER_HOURS - (-(num) % MINUTES_PER_HOURS)
    return f"{hours:02d}:{minutes:02d}"


print(time_of_day(0)) # == "00:00")        # True
print(time_of_day(-3)) # == "23:57")       # True
print(time_of_day(35)) # == "00:35")       # True
print(time_of_day(-1437)) # == "00:03")    # True
print(time_of_day(3000)) # == "02:00")     # True
print(time_of_day(800)) # == "13:20")      # True
print(time_of_day(-4231)) # == "01:29")    # True