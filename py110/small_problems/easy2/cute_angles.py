'''
P - Create a problem that takes a floating point number as an angle
        and returns a string containing the degrees, minutes, and seconds that 
        that angle represents. 
E -  E: The input angle must be between 0 and 360
        Use the ° symbol to represent degrees. (DEGREE = "\u00B0")
        Use ' to represent minutes
        Use " to represent seconds
        60 seconds in a minutes, 60 minutes in a degree. 
    IQ: Number to left of . is the degrees.
        The remaining decimal * 60 is the minutes
        The remaining decimal from that is seconds. 
D -  I: Integer
     O: String showing degrees, minutes, seconds, using proper symbols. 
     N: Number to left of . is the degrees.
        The remaining decimal * 60 is the minutes
        The remaining decimal from that is seconds.
A -  1. Define a function that takes a floating point number.
     2. Set three variables, degrees, seconds, minutes.
     3. Degrees is equal to the whole number of the floating point.
     4. Minutes is equal to the remainder of the decimal * 60.
     5. Seconds is equal to the remainer of the minutes * 60.
     6. Use formatted string to return degrees, seconds, minutes.
'''
degree_symbol = DEGREE = "\u00B0"
def dms(angle):
    degrees = int(angle)
    minutes = (angle - degrees) * 60
    seconds = (minutes - int(minutes)) * 60
    return f"{degrees}{degree_symbol}{int(minutes):02}'{int(seconds):02}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6)  == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")