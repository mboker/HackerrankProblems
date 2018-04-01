#!/bin/python3

import sys
from collections import defaultdict


def solve(arr, money):
    price_to_idx = {price: set() for price in arr}
    indexes = set()
    for idx, price in enumerate(arr):
        price_to_idx[price].add(idx)
    for price in price_to_idx.keys():
        if 2 * price == money:
            if len(price_to_idx[price]) == 2:
                indexes = price_to_idx[price]
                break
        elif money - price in price_to_idx.keys():
            indexes = (price_to_idx[price].pop(), price_to_idx[money - price].pop())
            break
    print(min(indexes)+1, max(indexes)+1)


if __name__ == "__main__":
    file = open('../tests/ice_cream_tables.txt')
    t = int(file.readline().strip())
    for a0 in range(t):
        money = int(file.readline().strip())
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split(' ')))
        solve(arr, money)