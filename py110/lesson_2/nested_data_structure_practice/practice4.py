'''
Given the object shown below, print the name, age, 
and gender of each family member:

Each output line should follow this patter: 
(name) is a (age)-year-old (male or female). 
'''

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for name, item in munsters.items():
    print(f"{name} is a {item['age']}-year-old {item['gender']}.")