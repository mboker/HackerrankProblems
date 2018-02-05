def num_ways(sum_val, numbers):
    return_val = 0
    for number in numbers :
        if number == sum_val:
            return_val +=1
        else:
            new_nums = [i for i in numbers if i <= sum_val - number and i < number]
            return_val += num_ways(sum_val - number, new_nums)
    return return_val

def is_perfect(num, pow_val):
    c = int(num**(1/float(pow_val)))
    return (c**pow_val == num) or ((c+1)**pow_val == num)

file = open('sum_of_powers.txt', 'r')

sum_value = int(file.readline().strip())
power = int(file.readline().strip())

perfects = []
for i in range(1, sum_value + 1):
    if is_perfect(i, power):
        perfects.append(i)

perfects.sort(reverse=True)
print(num_ways(sum_value, perfects))

