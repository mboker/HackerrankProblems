def dict_of_lists(it):
    dict = {}
    for key, val in it:
        if key in dict:
            dict[key].append(val)
        else:
            dict[key] = [val]
    return dict

file = open('ice_cream_parlor.txt', 'r')
t = int(file.readline().strip())
for trip in range(t):
    m = int(file.readline().strip())
    n = int(file.readline().strip())
    costs = file.readline().strip().split()
    costs = [int(cost) for cost in costs]
    costs_to_indexes = dict_of_lists((cost, index+1) for index, cost in enumerate(costs))
    costs = sorted(costs)
    pair, left, right = 0, 0, len(costs)-1
    while pair != m :
        pair = costs[left] + costs[right]
        if pair > m:
            right -= 1
        elif pair < m:
            left += 1
    left_index = costs_to_indexes[costs[left]][0]
    costs_to_indexes[costs[left]].pop(0)
    right_index = costs_to_indexes[costs[right]][0]
    print(min(left_index,right_index), max(left_index,right_index))