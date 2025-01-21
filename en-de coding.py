

def encode(x):
    c = []
    for i in range(len(x)):
        a = x[i]
        b = ord(a)
        b += 1
        c.insert(i, b)
    return c 

def decode(y):
    z = []
    for i in range(len(y)):
        a = y[i]
        a -= 1
        b = chr(a)
        z.insert(i, b)
    return z

def start():

    string = input("Enter a line: ")
    encoded = encode(string)

    decoded = decode(encoded)

    print(encoded)
    print(decoded)


start()
