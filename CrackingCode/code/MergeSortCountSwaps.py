#!/bin/python3
import sys

def mergeWithCount(arr):
    if len(arr) > 2:
        first_half_sorted, count_first = mergeWithCount(arr[:len(arr) // 2])
        second_half_sorted, count_second = mergeWithCount(arr[len(arr) // 2:])
        count_combined = 0
        sorted = []
        while len(first_half_sorted) > 0 or len(second_half_sorted) > 0:
            if len(first_half_sorted) == 0:
                sorted.append(second_half_sorted.pop(0))
            elif len(second_half_sorted) == 0:
                sorted.append(first_half_sorted.pop(0))
            elif second_half_sorted[0] < first_half_sorted[0]:
                sorted.append(second_half_sorted.pop(0))
                count_combined += 1
            else:
                sorted.append(first_half_sorted.pop(0))
        return sorted, count_combined + count_first + count_second
    elif len(arr) == 2:
        if arr[1] < arr[0]:
            arr.reverse()
            return arr, 1
    return arr, 0


def countInversions(arr):
    sorted, count = mergeWithCount(arr)
    return count


if __name__ == "__main__":
    file = open('../tests/merge_sort_count.txt')
    t = int(file.readline().strip())
    for a0 in range(t):
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split(' ')))
        result = countInversions(arr)
        print(result)