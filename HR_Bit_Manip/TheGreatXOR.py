def theGreatXor(x):
    values = 0
    index = 0
    while x > 0:
        if not x & 1:
            values += 2**index
        x = x >> 1
        index += 1
    return values

file = open('TheGreatXOR.txt', 'r')
q = int(file.readline().strip())
for a0 in range(q):
    x = int(file.readline().strip())
    result = theGreatXor(x)
    print(result)