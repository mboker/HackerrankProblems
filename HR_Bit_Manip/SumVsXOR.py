def solve(n):
    zeros = 0
    while n:
        if n & 1 == 0:
            zeros += 1
        n = n >> 1
    return 2**zeros

file = open('SumVsXOR.txt', 'r')
n = int(file.readline().strip())
result = solve(n)
print(result)
