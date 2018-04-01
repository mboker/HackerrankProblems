file = open('trip_to_moon.txt', 'r')

num_astros, num_pairs = file.readline().strip().split(' ')
num_astros, num_pairs = [int(num_astros), int(num_pairs)]
lone_astros = num_astros
astros = {i: [] for i in range(num_astros)}
for i in range(num_pairs):
    astro_1, astro_2 = file.readline().strip().split(' ')
    astro_1, astro_2 = [int(astro_1), int(astro_2)]
    astros[astro_1].append(astro_2)
    astros[astro_2].append(astro_1)
    for astro in astros[astro_1]:
        if astro_2 != astro:
            if not astro_2 in astros[astro]:
                astros[astro].append(astro_2)
            if not astro in astros[astro_2]:
                astros[astro_2].append(astro)
    for astro in astros[astro_2]:
        if astro_1 != astro:
            if not astro_1 in astros[astro]:
                astros[astro].append(astro_1)
            if not astro in astros[astro_1]:
                astros[astro_1].append(astro)

num_paired = 0
pairs = 0
remaining_to_check = list(astros.keys())
for key, astro in astros.items():
    remaining_to_check.remove(key)
    # potential pairs are total - 1 (for this one) - num_paired - group_size
    group = [val for val in astro if val in remaining_to_check]
    num_paired += 1
    pairs += len(remaining_to_check) - len(group)

print(pairs)