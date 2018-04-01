# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import itertools

def find_median(vals):
    midpoint = len(vals) // 2
    if len(vals) % 2 == 1:
        return vals[midpoint]
    else:
        return (vals[midpoint-1] + vals[midpoint])/2

file = open('../tests/interquartile_range.txt')
_ = file.readline()
nums = list(map(int, file.readline().strip().split()))
freqs = list(map(int, file.readline().strip().split()))
nums = [[num]*freqs[index] for index, num in enumerate(nums)]
nums = list(itertools.chain.from_iterable(nums))

nums.sort()
first_half = nums[:len(nums)//2]
second_half = nums[math.ceil(len(nums)/2):]

print(float(find_median(second_half) - find_median(first_half)))
