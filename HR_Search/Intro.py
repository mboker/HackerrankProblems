file = open('intro.txt', 'r')
value = int(file.readline().strip())
_ = file.readline()
arr = list(map(int, file.readline().strip().split()))

left = 0
right = len(arr)
found = False
while left < right and not found:
    middle = left+(right-left)//2
    if arr[middle] == value:
        print(middle)
        found = True
    elif arr[middle] < value:
        left = middle
    elif arr[middle] > value:
        right = middle