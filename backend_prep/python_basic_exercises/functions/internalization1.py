def greet(language):
    match language:
        case 'en':
            return ('Hi!')
        case 'fr':
            return ('Salut!')
        case 'pt':
            return ('Ola!')
        case 'de':
            return ('Hallo!')
        case 'sv':
            return ('Hej!')
        case 'af':
            return ('Haai!')
        case _:
            return ("I don't recognize that language!")

print(greet('en'))
print(greet('fr'))
print(greet('pt'))
print(greet('de'))
print(greet('sv'))
print(greet('af'))
print(greet('ka'))