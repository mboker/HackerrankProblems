cost = 0


def connect_children(cities, connected_cities, cost_road):
    for _, connected_city in connected_cities.items():
        if not connected_city['library']:
            connected_city['library'] = True
            global cost
            cost += cost_road
            children_cities = {key: cities[key] for key in connected_city['connections']
                               if not cities[key]['library']}
            connect_children(cities, children_cities, cost_road)


file = open('libs_and_roads.txt', 'r')
q = int(file.readline().strip())
for a0 in range(q):
    n_cities, n_roads, cost_lib, cost_road = file.readline().strip().split(' ')
    n_cities, n_roads, cost_lib, cost_road = [int(n_cities), int(n_roads), int(cost_lib), int(cost_road)]

    cities = {i+1: {'connections': [], 'library': False} for i in range(n_cities)}
    for a1 in range(n_roads):
        city_1, city_2 = file.readline().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        cities[city_1]['connections'].append(city_2)
        cities[city_2]['connections'].append(city_1)

    global cost
    cost = 0
    if cost_road >= cost_lib:
        cost = n_cities * cost_lib
    else:
        for city_key, city in cities.items():
            if not city['library']:
                city['library'] = True
                cost += cost_lib
                connected_cities = {connected_key: cities[connected_key] for connected_key in city['connections']
                                    if not cities[connected_key]['library']}
                connect_children(cities, connected_cities, cost_road)

    print(cost)
