#!/bin/python3
import sys

def merge_with_count(arr):
    if len(arr) > 2:
        first_half_sorted, count_first = merge_with_count(arr[:len(arr) // 2])
        second_half_sorted, count_second = merge_with_count(arr[len(arr) // 2:])
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


def count_inversions(arr):
    sorted, count = merge_with_count(arr)
    return count


def merge_with_count_in_place(arr, start, end):
    length = end - start
    total = 0
    if length == 1:
        return 0
    if length == 2 and arr[end - 1] < arr[start]:
        arr[end - 1], arr[start] = arr[start], arr[end - 1]
        return 1
    elif length > 2:
        mid = start + (end - start) // 2
        left_count, right_count = merge_with_count_in_place(arr, start, mid), merge_with_count_in_place(arr, mid, end)
        left, right = start, mid
        while left < mid and right < end:
            if arr[right] < arr[left]:
                # move [right] into left position, and shift left half over 1 location
                arr[left + 1:right + 1], arr[left] = arr[left:right], arr[right]
                total += right - left
                mid, right = mid + 1, right + 1
            left += 1
        total += left_count + right_count
    return total


def count_inversions_in_place(arr):
    count = merge_with_count_in_place(arr, 0, len(arr))
    return count



if __name__ == "__main__":
    file = open('../tests/merge_sort_count.txt')
    t = int(file.readline().strip())
    for a0 in range(t):
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split(' ')))
        result = count_inversions(arr)
        print(result)