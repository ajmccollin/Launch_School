def swap_name(name):
    split_name = name.split()
    return split_name[1] + ', ' + split_name[0]

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True