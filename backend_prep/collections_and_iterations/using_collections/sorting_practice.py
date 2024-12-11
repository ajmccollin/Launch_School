my_list = ['Steve', 'john', 'Alex', 'Will']   
my_list.sort()                                #Case sensitive
print(my_list)      

my_list.sort(key=str.lower)                   #Case insensitive
print(my_list)                                

my_list.sort(reverse=True)                    #Reverse order
print(my_list)                                

my_list.sort(key=str.lower, reverse=True)     #Reverse orders, case insensitive
print(my_list)                                

number_list = ['100', '431', '10', '13', '41', '5', '15']
number_list.sort()                            #Not sorted by int
print(number_list)                            


number_list.sort(key=int)                     #Sorted by integer
print(number_list)                            

number_list.sort(key=int, reverse=True)
print(number_list)