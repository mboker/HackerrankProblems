def sort_sub_array(arr):
    e = arr[len(arr)-1]
    sub_done = False
    i = len(arr) - 1
    while not sub_done:
        if i == 0:
            arr[i] = e
            sub_done = True
        else:
            if arr[i-1] <= e and arr[i] >= e:
                arr[i] = e
                sub_done = True
            else:
                arr[i] = arr[i-1]
        i -= 1
    return arr

file = open('insertion2.txt', 'r')
_ = file.readline()
array = list(map(int, file.readline().strip().split()))
if len(array) == 1:
    print(array[0])
sorted_idx = 2
while sorted_idx <= len(array):
    array[:sorted_idx] = sort_sub_array(array[:sorted_idx])
    print(' '.join(map(str,array)))
    sorted_idx += 1
