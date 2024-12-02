#ask for user name
#greet the user

#if user has ! at the end of their name, yell with greeting

user_name = input("What's your name? ")

if user_name[-1] == '!' :
    print(f'HELLO {user_name.upper()}!! WHY ARE WE YELLING!!')
else:
    print(f'Hello {user_name}.')