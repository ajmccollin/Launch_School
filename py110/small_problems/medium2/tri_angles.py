'''
P - Create a function that takes three integers as an argument and returns the 
        the type of triangle being passed through.
E - E:  2 immediate requirements:
        The three integer arguments must equal 180 total
        Each integer must be greater than 0.
            If these conditions are not met, then the string `invalid` is returned.
        If one angle is exactly 90, return 'right'
        If one angle is greater than 90, return `obtuse`
        If all angles are less than 90, return `acute`.
        The integer passed will always be an integer and in degrees.
    IQ: 
D - I:  Three integer values.
    O:  A string determining what kind of triangle is being passed, if any.
    N:  Might want to use two functions, one to determine a valid triangle,
            and another to determine the kind of triangle.
        Iteration over each one to see if any are equal to or greater than 90.
A - 1. Create a function called `valid_triangle` that takes the three nums as 
        the argument.
    2. Use the if all() function to determine if any values are equal to 0.
    3. In the conditional, return all three angles equaling to 180.
    4. Return false if the conditional is not true.
    
    Perhaps create a list and have valid triangle take one argument.
    1. Create a function called triangle that takes three integers as the
            argument.
    2. Create a list of the three integers and call the valid_triangle function
            on the list using an if statment.
    3. If the conditional is not met, return `invalid`.
    4. Otherwise, if any angle is greater than 90, return obtuse.
        if any angle is exactly equal to 90, return `equilateral`
        if all angles are less than 90, return `acute`.
'''
def valid_triangle(angles):
    if all(angle > 0 for angle in angles):
        return sum(angles) == 180
    return False

def triangle(angle1, angle2, angle3):
    angles_lst = [angle1, angle2, angle3]
    
    if valid_triangle(angles_lst):
        if 90 in angles_lst:
            return 'right'
        elif any(angle > 90 for angle in angles_lst):
            return 'obtuse'
        else:
            return 'acute'
    return 'invalid'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True