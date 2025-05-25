'''Compute and display the total age of the family's male members. '
Try working out the answer two ways: first with an ordinary loop, '
'then with a comprehension.'''

# [output_expression for item in existing_list if condition]

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

def male_age(lst):
    total_age = {value['age'] for value in munsters.values() 
                 if value['gender'] == 'male'}
    return sum(total_age)

print(male_age(munsters))