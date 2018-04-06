import os
import sys


#
# Complete the dynamicArray function below.
#
from collections import defaultdict
def dynamicArray(n, queries):
    seq_list, last_answer = defaultdict(list), 0
    answer = []
    for query in queries:
        if query[0] == 1:
            seq_list[(query[1] ^ last_answer) % n].append(query[2])
        else:
            seq = seq_list[(query[1] ^ last_answer) % n]
            last_answer = seq[query[2] % len(seq)]
            answer.append(last_answer)
    return answer


if __name__ == '__main__':
    file = open('dynamic-array.txt')

    nq = file.readline().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, file.readline().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))