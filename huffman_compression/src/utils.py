def get_frequency(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def write_to_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)