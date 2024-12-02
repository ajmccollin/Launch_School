obj = 42

obj = 'ABcd' #reassign
obj.upper() #neither
obj = obj.lower() #reassign
print(len(obj)) #neither
obj = list(obj) #reassign
obj.pop() #mutate
object[2] = 'X' #mutate
obj.sort() #mutate
set(obj) #neither
obj = tuple(obj) #reassign