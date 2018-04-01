from min_max_heap import MinMaxHeap

# if __name__ is '__main__':
f = open('test_input2.txt', 'r')
n = int(f.readline().strip())
a = MinMaxHeap()
a_i = 0
for a_i in range(n):
    a_t = int(f.readline().strip())
    a.append(a_t)


