def greetings(list, dict):
    name = ' '.join(list)
    return (f'Hello, {name}! Nice to have a '
            f'{dict["title"]} {dict["occupation"]} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)