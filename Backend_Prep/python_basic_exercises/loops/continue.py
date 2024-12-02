cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for name in cities:
    if name == None:
        continue
    print(len(name))