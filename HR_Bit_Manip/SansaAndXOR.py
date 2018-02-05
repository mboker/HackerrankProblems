def reduce_array(array):
    if len(array) % 2 == 0:
        return 0
    else:
        result = 0
        for i in range(int(len(array)/2) + 1):
            result = result ^ array[2*i]
        return result

    # for sub_length in range(1, len(array) + 1):
    #     for i in range(len(array)- sub_length + 1):
    #         sub_array = array[i : sub_length+i]
    #         for element in sub_array:
    #             result = result ^ element
    # return result


file = open('SansaAndXOR.txt','r')
num_cases = int(file.readline().strip())
for case in range(num_cases):
    arr_size = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))
    print(reduce_array(arr))