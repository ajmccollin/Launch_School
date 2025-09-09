'''
P - Create a function that returns a new list where each element is the product
        of two cooresponding integers from two different lists.
E -  E: - Two lists of the same length
        - A new list is returned with the product of the two integers from the 
            list
     I: The input will always be valid with a valid integers
D -  I: Two lists containing integers
     O: One list with the product of two cooresponding integers.
     H: might use zip function?
A - 1. Define a function called `mulitiply_items` that takes two parameters,
        `list_a` and `list_b`.
    2. Return a comprehension that does the following
        3. Call the zip function for the two lists and iterate over the pairs.
        4. Return the product of the pairs within a list comprehension. 
            5. 
'''
def multiply_items(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True