'''Sort the following list of numbers first in ascending numeric order, 
then in descending numeric order, mutating the list. '''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)