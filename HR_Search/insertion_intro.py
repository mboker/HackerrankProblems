file = open('insertion_intro.txt', 'r')
_ = file.readline()
arr = list(map(int, file.readline().strip().split()))
e = arr[len(arr)-1]
done = False
i = len(arr) - 1
while not done:
    if i == 0:
        arr[i] = e
        done = True
    else:
        if arr[i-1] <= e and arr[i] > e:
            arr[i] = e
            done = True
        else:
            arr[i] = arr[i-1]
    print(' '.join(map(str,arr)))
    i -= 1