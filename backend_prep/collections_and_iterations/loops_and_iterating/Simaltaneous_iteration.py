object_name = ['Toyota', 'Cow', 'Jimmy Hendricks', 'Dutch Bros', 'Alien', 
               'Alligator']
object_type = ['Car', 'Animal', 'Musician', 'Coffee Shop', 'Creature',
                'Animal']
vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
zipped_names = zip(object_name, object_type)
for object_name, object_type in zipped_names:
    if object_name.startswith(vowels):
        print(f'An {object_name} is a type of {object_type}')
    else:
        print(f'A {object_name} is a type of {object_type}')