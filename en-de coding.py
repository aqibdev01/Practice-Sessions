def encode(to_encode):
    encoded_array = []
    for i in range(len(to_encode)):
        ascii_value = ord(to_encode[i])
        encoded = ascii_value + 1
        encoded_array.insert(i, encoded)
    return encoded_array

def decode(to_decode):
    decoded_array = []
    for i in range(len(to_decode)):
        encoded_value = to_decode[i]
        in_ascii = encoded_value - 1
        decoded = chr(in_ascii)
        decoded_array.insert(i, decoded)
    return decoded_array

def start():

    string = input("Enter a line: ")
    encoded = encode(string)
    print(encoded)

    choice_for_decode = input("Do you want to decode this output? (y/n) ")
    if choice_for_decode.lower() == 'y':
        decoded = decode(encoded)
        print(decoded)
    else:
        pass

    another_try = input("Do you want to encode another string? (y/n) ")
    if another_try == 'y':
        start()
    else:
        print("Bye")


start()
