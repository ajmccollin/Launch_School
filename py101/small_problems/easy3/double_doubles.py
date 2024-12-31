#double number: first half is the same as the second half
def twice(int_value):
    half_value = (int_value) // 2
    if int_value[0, half_value] == int_value[half_value, int_value]:
        return int_value
    else:
        return int(int_value) * 2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 8 == 767688)        # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676))                      # True