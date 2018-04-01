from collections import defaultdict, OrderedDict


class Graph:
    def __init__(self, num_nodes):
        self.nodes = defaultdict(set)
        self.max = num_nodes

    def connect(self, node1, node2):
        self.nodes[node1].add(node2)
        self.nodes[node2].add(node1)

    def find_all_distances(self, source_node):
        distances = []
        for idx in range(self.max):
            dest_node = idx + 1
            if dest_node != source_node:
                distances.append(self.find_distance(source_node, dest_node))

        print(' '.join(list(map(str, distances))))

    def find_distance(self, source_node, dest_node):
        searched = set()
        current_node = source_node
        searched.add(source_node)
        searching = OrderedDict()
        searching.update({node: 1 for node in self.nodes[source_node]})
        searched.update(self.nodes[source_node])
        while len(searching) > 0:
            if dest_node in searching.keys():
                return searching[dest_node] * 6
            current_node = list(searching.keys())[0]
            current_dist = searching.pop(current_node) + 1
            searching.update({node: current_dist for node in self.nodes[current_node] if node not in searched})
            searched.update(self.nodes[current_node])
        return -1


file = open('../tests/BFS.txt')
t = int(file.readline())
for i in range(t):
    n, m = [int(value) for value in file.readline().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in file.readline().split()]
        graph.connect(x, y)
    s = int(file.readline())
    graph.find_all_distances(s)