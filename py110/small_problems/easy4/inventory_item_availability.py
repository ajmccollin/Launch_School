'''
P - Create a function that returns a boolean depending on whether the item is
    in stock.
E - I: list of transactions and item id
    O: Boolean
    E:  - The key 'movement' determines whether the item is `in` or `out`
            - in adds while out subtracts, essentially.
            - A quantity of 5 in adds 5, a quantity of 5 out subtracts 5
        - If the total quantity (after in/out) is greater than 0, return True,
            otherwise return False
        - Will need to access each item based on item
        - Might be helpful to add a quantity counter.
D - Will have to use key access for each dictionary item, return a boolean
A - 1. Define a function called `is_item_available` that takes an item id and
        the transaction as the parameters.
    2. Paste function from previous exercise to access an item. 
    3. Create a total_sum counter and set to 0
    4. Call `transactions_for` function and iterate over each returned
        transaction.
        - Access key for movement, add/subtract quantity for in/out respectively
    5. If quantity is greater than 0, return True. Otherwise return False. 
'''

def transactions_for(item_id, transactions):
    return [transaction for transaction in transactions
            if transaction['id'] == item_id]

def is_item_available(item_id, transactions):
    total_quantity = 0
    for transaction in transactions_for(item_id, transactions):
        if transaction['movement'] == 'in':
            total_quantity += transaction['quantity']
        elif transaction['movement'] == 'out':
            total_quantity -= transaction['quantity']
    return total_quantity > 0

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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True