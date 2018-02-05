import sys
import math


def number_of_moves(counter):
    if counter == 1:
        return 0
    elif math.log(counter, 2) % 1 > 0.00000001:
        return 1 + number_of_moves(counter ^ (2**math.floor(math.log(counter, 2))))
    else:
        return 1 + number_of_moves(counter>>1)


file = open('CounterGame.txt', 'r')
test_cases = int(file.readline().strip())
for i in range(test_cases):
    num_moves = number_of_moves(int(file.readline()))
    print ('Louise' if num_moves % 2 == 1 else 'Richard')