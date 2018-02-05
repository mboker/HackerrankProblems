import sys
import math

file = open('AndProduct.txt', 'r')
q = int(file.readline().strip())
line = 0
while line < q:
    n, m = file.readline().strip().split(' ')
    n, m = [int(n), int(m)]
    if m > n:
        digits = math.log(m - n, 2)
        output = n
        for i in range(math.ceil(digits)):
            output = output & (n + 2 ** i)
        output = output & m
    line += 1
    print(output)