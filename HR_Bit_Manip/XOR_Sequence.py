def xor_seq(L,R):
    result = 0
    left_partial = (4 - (L % 4)) % 4
    for num in range(L, L+left_partial):
        if num % 4 == 0:
            result = result ^ num
        elif num % 4 == 1:
            result = result ^ 1
        elif num % 4 == 2:
            result = result ^ (num ^ 1)
        else:
            result = result ^ 0
    right_partial = R % 4
    for num in range(R-right_partial, R+1):
        if num % 4 == 0:
            result = result ^ num
        elif num % 4 == 1:
            result = result ^ 1
        elif num % 4 == 2:
            result = result ^ (num ^ 1)
        else:
            result = result ^ 0
    middle = R - right_partial - (L + left_partial)
    if (middle//4) % 2 == 1:
        result = result ^ 2
    return result

file = open('XORSequence.txt', 'r')

Q = int(file.readline().strip())
for a0 in range(Q):
    L,R = file.readline().strip().split(' ')
    L,R = [int(L),int(R)]
    print(xor_seq(L,R))