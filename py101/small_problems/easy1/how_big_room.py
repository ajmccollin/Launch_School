print('Please enter the length of the room (in meters): ')
room_length = float(input())

print('Please enter the width of the room (in meters): ')
room_width = float(input())

room_in_meters = room_length * room_width
room_in_feet = room_in_meters * 10.7639

print(f'The room is {room_in_meters:.2f} square meters and '
      f'{room_in_feet:.2f} square feet.')