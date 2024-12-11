destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, list):
    for cities in list:
        if cities == city:
            return True
    return False

print(contains('Barcelona', destinations)) # True
print(contains('Nashville', destinations)) # False