'''
P: Create a function with two arguments, an item ID and a list of transactions
    and return the list of transactions for the specified item ID. 
E: There needs to be two parameters, item and transaction. 
    All transactions for the specified key should be returned.
D: Will be utilizing dictionaries, so use of keys, items, and values will most
    likely be necessary.
A:  1.Create a function called `transactions_for` that takes the parameters
    `item_id` and `transactions`
    2. Create an empty list called item_transactions.
    3. iterate over each item in the list. if the key `id` is equal to the id 
    argument, append the entire item to the item_transactions list.
    4. Return item_transactions or condense into a list comprehension and 
        return that comprehension value. 
    
C:
'''
def transactions_for(item_id, transactions):
    item_transactions = []

    for sets in transactions[0]:
        for item in sets:
            if item['id'] == item_id:
                item_transactions.append(item)

    return item_transactions


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions)) # ==
    #   [
    #       {"id": 101, "movement": "in",  "quantity":  5},
    #       {"id": 101, "movement": "in",  "quantity": 12},
    #       {"id": 101, "movement": "out", "quantity": 18},
    #   ]) # True