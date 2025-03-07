def calculate_meters(num1, num2):
    area = float(num1) * float(num2)
    return area

def convert_feet(num1):
    return (num1 * 10.7639)

def invalid_float(num1):
    try:
        number = float(num1)
        if number <= 0:
            raise ValueError
    except ValueError:
            return True
    return False


width = input('Please enter the length of the room in meters: ')
while invalid_float(width):
    print('Please enter a valid number greater than 0: ', end = '')
    width = input()

length = input('Please enter the width of the room in meters: ')
while invalid_float(length):
    print('Please enter a valid number greater than 0: ', end = '')
    length = input()


room_in_meters = calculate_meters(width, length)
room_in_feet = convert_feet(room_in_meters)

print(f'The room is {room_in_meters} '
      f'square meters and {room_in_feet} square feet')