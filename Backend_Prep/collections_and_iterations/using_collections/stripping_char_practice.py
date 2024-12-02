'''
text = ' \t abc def      \n\r'
print(text)

print(text.strip())
print(repr(text.strip()))
'''

'''
text = 'This     is     a             string!'
print(text.split())
print(text.split(' '))
'''

words = ['Hi', 'I', 'Am', 'A', 'String']
print('!! '.join(words))
print(' '.join(words))