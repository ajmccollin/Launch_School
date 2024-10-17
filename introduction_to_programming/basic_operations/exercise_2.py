my_num = 4936

ones = (my_num % 10)
my_num = my_num // 10  #493
print('Ones values is:', ones)

tens = (my_num % 10)
my_num = my_num // 10 #49
print('Tens values is:', tens)

hundreds = (my_num % 10)
my_num = my_num // 10 #4
print('Hundreds values is:', hundreds)

thousands = my_num
print('Thousands values is:', thousands)

print(thousands, hundreds, tens, ones)