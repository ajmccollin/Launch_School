def xor(value1, value2):
    if value1:
        if not value2:
            return True
        elif value2:
            return False
    else:
        if value2:
            return True
        else:
            return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)


#Simplified down
def xor2(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True
    return False
    
print(xor2(5, 0) == True)
print(xor2(False, True) == True)
print(xor2(1, 1) == False)
print(xor2(True, True) == False)