def calculate_leftover_blocks(starting_blocks):
    current_layer = 1
    remaining_blocks = starting_blocks
    while remaining_blocks >= current_layer ** 2:
        remaining_blocks -= current_layer ** 2
        current_layer += 1
    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)
print(calculate_leftover_blocks(1) == 0)
print(calculate_leftover_blocks(2) == 1)
print(calculate_leftover_blocks(4) == 3)
print(calculate_leftover_blocks(5) == 0)
print(calculate_leftover_blocks(6) == 1)
print(calculate_leftover_blocks(14) == 0)
print(calculate_leftover_blocks(100) == 9)
print(calculate_leftover_blocks(1000) == 181)

