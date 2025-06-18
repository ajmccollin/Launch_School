def count_occurrences(vehicles):
    vehicle_count = {}
    for vehicle_type in vehicles:
        vehicle_count[vehicle_type] = vehicle_count.get(vehicle_type, 0) + 1

    for vehicle_type, count in vehicle_count.items():
        print(f'{vehicle_type} => {count}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)