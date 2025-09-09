'''
P - Create a function that determines what kind of triangle is present based
        on three integer inputs.
E - E:  Three types of triangles:
            equilateral - all three sides are equal
            isosceles - two sides are the same, one side is different
            scalene - All three sides are different lengths.

        Sides must all be greater than 0.
        Additionally, the two shorter numbers must combine to be greater than 
            the larger number.
            *** If these two requirements are not met, the triangle is invalid
                and should return `invalid`.
    I/Q: There are always going to be 3 integers passed as the argument.
         The sides can be floats.
D - I: Three integer numbers.
    O: One of four strings: `equilateral`, `isosceles`, `scalene` or `invalid`
    N: Determine the largest of the three numbers and add the two shorter ones
            to determine if the triangle is valid
        If any sides are equal to 0, return Invalid always.
A - 1. Define a function called `valid_triangle` that takes the three inputs. 
        a. Return false if any value is equal to 0
        b. Create a list of all three values.
        c. max value is equal to the popped max value from the list.
        d. return sum of list is greater than max value. 
    2. Define a function called triangle that takes three integers as arguments
        a. call valid triangle on the three arguments
        b. if all 3 values are the same, return equilateral
        c. if 2 values are the same, return isosceles.
        d. if all 3 values are different, return scalene
'''
def valid_triangle(sides):
    if all(sides):
        ascending_length = sorted(sides)
        side_a, side_b, side_c = ascending_length
        return side_a + side_b > side_c
    return False

def triangle(side1, side2, side3):
    all_sides = [side1, side2, side3]
    unique_sides = set(all_sides)

    if valid_triangle(all_sides):
        if len(unique_sides) == 1:
            return 'equilateral'
        elif len(unique_sides) == 2:
            return 'isosceles'
        elif len(unique_sides) == 3:
            return 'scalene'
    else:
        return 'invalid'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True