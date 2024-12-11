weather = input("What's the weather today? ")

match weather:
    case 'rainy':
        print('Make sure to grab your umbrella!')
    case 'sunny':
        print("It's a good day to go outside!")
    case 'snowy':
        print('Make sure to wear a coat, hat, and gloves!')
    case _:
        print('Hmm not sure. Best to stay inside today!')