def is_empty_or_blank(collection):
    return collection.isspace() or len(collection) == 0

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True