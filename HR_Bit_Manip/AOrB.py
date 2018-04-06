#!/bin/python3

import os
import sys
import math


#
# Complete the aOrB function below.
#
def aOrB(k, a, b, c):
    changed = 0
    a, b, c = int(a, 16), int(b, 16), int(c, 16)
    a_turn_off = (a | c) ^ c
    a_prime = a ^ a_turn_off
    b_turn_off = (b | c) ^ c
    b_prime = b ^ b_turn_off

    a_and_b_turn_off = a_turn_off & b_turn_off
    a_xor_b_turn_off = a_turn_off ^ b_turn_off
    while a_and_b_turn_off > 0:
        highest_bit = math.floor(math.log(a_and_b_turn_off, 2))
        a_and_b_turn_off ^= 2 ** highest_bit
        changed += 2
    while a_xor_b_turn_off > 0:
        highest_bit = math.floor(math.log(a_xor_b_turn_off, 2))
        a_xor_b_turn_off ^= 2 ** highest_bit
        changed += 1
    if changed > k:
        print(-1)
        return

    turn_on = c ^ (a_prime | b_prime)
    activate_value = 0
    while turn_on > 0:
        highest_bit = math.floor(math.log(turn_on, 2))
        turn_on ^= 2 ** highest_bit
        b_prime |= 2 ** highest_bit
        changed += 1
    if changed > k:
        print(-1)
        return

    highest_bit = math.floor(math.log(a_prime, 2))
    while changed < k and highest_bit > 0:
        mask = 2 ** highest_bit
        if b_prime & mask:
            a_prime ^= mask
            changed += 1
        elif changed < k - 1:
            a_prime ^= mask
            b_prime |= mask
            changed += 2
        mask -= 1
        highest_bit = math.floor(math.log(max(a_prime & mask,1), 2))

    print(format(a_prime, 'x').upper())
    print(format(b_prime, 'x').upper())

if __name__ == '__main__':
    file = open('AOrB.txt')
    q = int(file.readline())

    for q_itr in range(q):
        k = int(file.readline())

        a = file.readline()

        b = file.readline()

        c = file.readline()

        aOrB(k, a, b, c)