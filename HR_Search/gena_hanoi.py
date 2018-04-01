from collections import defaultdict


def build_towers(arr):
    towers = defaultdict(list)
    for disc, tower in enumerate(arr):
        towers[tower].insert(0, disc+1)
    return towers


def get_moves(towers, discs):
    moves = []
    for tower in towers.keys():
        top = len(tower) - 1
        if top >= 0:
            if towers[tower][top] != discs:



def search_moves(towers, discs):
    moves = get_moves(towers, discs)
    while len(moves) > 0:
        pass


def solve_towers(arr):
    discs = len(arr)
    towers = build_towers(arr)
    return search_moves(towers, discs)


file = open('gena_hanoi.txt', 'r')

N = int(file.readline().strip())
a = [int(a_temp) for a_temp in file.readline().strip().split(' ')]
print(solve_towers(a))