user_name = input("What is your name? ")
if user_name.endswith('!'):
    print(f'HELLO {user_name.upper()}! WHY ARE WE YELLING?')
else:
    print(f'Hello {user_name}.')