store = {}


def calculate(n):
    if n in store.keys():
        return store[n]
    elif n==1:
        store[n] = 1
    elif n==2:
        store[n] = 2
    elif n==3:
        store[n] = 4
    else:
        store[n] = calculate(n-1) + calculate(n-2) + calculate(n-3)
    return store[n]

file = open('../tests/recursion_stairs.txt')
s = int(file.readline().strip())
for a0 in range(s):
    n = int(file.readline().strip())
    calculate(n)
    print(store[n])