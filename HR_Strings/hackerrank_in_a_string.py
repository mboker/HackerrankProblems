#!/bin/python3
def contains_hackerrank(word):
    contains = True
    index = 0
    for character in 'hackerrank':
        index = word.find(character, index)
        if index == -1:
            contains = False
            break
    return contains

file = open('hackerrank_in_a_string.txt', 'r')
q = int(file.readline().strip())
for a0 in range(q):
    s = file.readline().strip()
    if contains_hackerrank(s):
        print('YES')
    else:
        print('NO')