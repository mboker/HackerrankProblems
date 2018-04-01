#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    a = sorted(a)
    left, right = 0, 1
    answer = 0
    while right < len(a) and left < right:
        dif = a[right] - a[left]
        if dif == k:
            answer += 1
            right += 1
            left += 1
        elif dif > k:
            left += 1
            if left == right:
                right += 1
        else: # dif < k
            right += 1
    return answer

file = open('pairs.txt', 'r')
_, k = file.readline().strip().split()
k = int(k)
vals = file.readline().strip().split()
vals = [int(val) for val in vals]

print(pairs(vals, k))
