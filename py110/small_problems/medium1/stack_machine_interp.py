'''
P -  Create a function that implements miniature stack-register program that
        follows several different commands. 
E -  E: These are the following commands:
            n - places an integer into the register
            push - push register value onto stack, leave in register
            add - pop value from stack and add to register
            sub - pop value from stack and subtract from register
            mult - pop value and multiply value to register
            div - pop value to stack and divide register value to stack
            remainder - pop value from stack and store remainder in register
            pop - remove topmost value from stack and place in register.
            print - print value in register.
    IQ: There will always be a variable in the stack/ first command will be a
            value n being stored to the stack. 
D -  I: String
     O: Integer values printed out
     N: Will want to have a blank variable called `register` that values are
            stored to. 
A - 1. Create a function called `minilang` that takes a string as the input
    2. Split the input string.
    3. Initialize an empty list and assign it to the variable 'stack'
    4. Initialize the variable `register` and assign it to the int 0.
    5. Iterate over each split string with the following match/case.
            integer - place on stack
            push - push stack value onto stack
            add - add stack to register
            sub - subtract last stack value to register
            mult = multiply last stack value to register
            div - divide last stack value to register
            remainder - pop value from stack and store the remainder of int 
                division to register
            pop - remove topmost value and place in register
            print - print register value.

'''
def minilang(input_str):
    stack = []
    register = 0

    for command in input_str.split():
        match command:
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()
            case 'POP':
                register = stack.pop()
            case 'PRINT':
                print(register)
            case _:
                register = int(command)

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)