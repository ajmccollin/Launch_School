def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element] #This buffer is a new local variable
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

buffer_size = 5
buffer = ['there']
new_element = ['hello']

add_to_rolling_buffer1(buffer, buffer_size, new_element)
'''add_to_rolling_buffer2(buffer, buffer_size, new_element)'''
print(buffer)

