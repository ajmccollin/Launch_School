MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def clock_to_times(time):
    hours = int(time.split(":")[0]) # isolate hours from 24 hr clock
    minutes = int(time.split(":")[1]) # isolate minutes from 24 hr clocks

    return [hours, minutes]

def after_midnight(time):
    hours, minutes = (clock_to_times(time))

    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time):
    minutes = MINUTES_PER_DAY - after_midnight(time)
    if minutes == MINUTES_PER_DAY:
        minutes = 0

    return minutes

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True