#!/bin/python3

import sys


def sort(array):
    heap = min_heapify(array)
    index = 0
    while len(heap) > 1:
        array[index] = heap[1]
        remove_head_from_heap(heap)
        index += 1
    return array


def min_heapify(array):
    heap = [None, array[0]]
    for value in array[1:]:
        heap.append(value)
        fix_heap_from_leaf(heap)
    return heap


def fix_heap_from_leaf(heap):
    new_node_pos = len(heap) - 1
    parent_node_pos = int(new_node_pos / 2)
    while new_node_pos > 1:
        if string_lt(heap[new_node_pos], heap[parent_node_pos]):
            heap[new_node_pos], heap[parent_node_pos] = heap[parent_node_pos], heap[new_node_pos]
            new_node_pos = parent_node_pos
            parent_node_pos = int(new_node_pos / 2)
        else:
            break


def string_lt(string1, string2):
    if len(string1) < len(string2):
        return True
    elif len(string2) < len(string1):
        return False
    else:
        return string1 < string2


def remove_head_from_heap(heap):
    heap[1] = heap[len(heap)-1]
    heap.pop()
    head, child_one, child_two = 1, 2, 3
    while child_one < len(heap):
        greater_than_child_one = string_lt(heap[child_one], heap[head])
        greater_than_child_two = False
        if child_two < len(heap):
            greater_than_child_two = string_lt(heap[child_two], heap[head])

        if greater_than_child_one and greater_than_child_two:
            if string_lt(heap[child_one],heap[child_two]):
                heap[child_one], heap[head] = heap[head], heap[child_one]
                head = child_one
            else:
                heap[child_two], heap[head] = heap[head], heap[child_two]
                head = child_two
        elif greater_than_child_one:
            heap[child_one], heap[head] = heap[head], heap[child_one]
            head = child_one
        elif greater_than_child_two:
            heap[child_two], heap[head] = heap[head], heap[child_two]
            head = child_two
        else:
            break

        child_one, child_two = 2 * head, 2 * head + 1

file = open('input.txt', 'r')
n = int(file.readline().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(file.readline().strip())
    unsorted.append(unsorted_t)

for val in sort(list(unsorted)):
    print(val)
