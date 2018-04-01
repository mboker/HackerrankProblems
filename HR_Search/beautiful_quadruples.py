
def pairs(x, y):
    pairs = {}
    for i in range(1, x+1):
        for j in range(i, y+1):
            pairs[(i, j)] = (i ^ j)
    return pairs

def number_of_quads(a, b, c, d):
    numbers = sorted([a, b, c, d])
    pairs_first_two = pairs(numbers[0], numbers[1])
    pairs_second_two = pairs(numbers[2], numbers[3])
    results = set()
    for first_pair in pairs_first_two.items():
        for second_pair in pairs_second_two.items():
            if first_pair[1] ^ second_pair[1] > 0:
                results.add(tuple(sorted([first_pair[0][0], first_pair[0][1], second_pair[0][0], second_pair[0][1]])))
    return len(results)




file = open('beautiful_quads.txt', 'r')
A, B, C, D = file.readline().strip().split(' ')
A, B, C, D = [int(A), int(B), int(C), int(D)]
print(number_of_quads(A, B, C, D))
