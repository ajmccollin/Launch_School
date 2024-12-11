pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

print(pets.get('Dog'))
print(pets.get('Lizard'))
#pets['Lizard'] = '<silence>'
#print(pets.get('Lizard'))

#or 
print(pets.get('Lizard', '<silence>'))