def extract_language(locale):
    return locale[:2]

def extract_region(locale):
    return locale[3:5]
    
def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    if language == 'en':
        match region:
            case 'US':
                return ('Hey!')
            case 'GB':
                return ('Hello!')
            case 'AU':
                return ('Howdy!')
    else:
        match language:
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
        
print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))

print(local_greet('af_LA.UTF-8'))
print(local_greet('sv_ET.UTF-8'))