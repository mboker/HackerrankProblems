
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = set()
        self.connections = set()
        self.tree = None

    def __lt__(self, other):
        return len(self.connections) < len(other.connections)


class Tree:
    def __init__(self, node_idx):
        self.nodes = set(node_idx)
        self.root = node_idx

    def is_complete(self):
        return len(self.nodes) % 2 == 0


def add_connections(nodes_obj, edges_num):
    for edge in range(edges_num):
        node1, node2 = file.readline().strip().split()
        node1, node2 = int(node1), int(node2)
        nodes_obj[node1].connections.add(node2)
        nodes_obj[node2].connections.add(node1)


def build_tree(ordered_nodes_list, nodes_dict):
    single_connect_nodes_list = [node_obj for node_obj in ordered_nodes_list if len(node_obj.connections) == 1]
    while len(single_connect_nodes_list) > 0:
        for node in single_connect_nodes_list:
            if len(node.connections) > 0:
                node.parent = node.connections.pop()
                nodes_dict[node.parent].children.add(node.key)
                nodes_dict[node.parent].connections.remove(node.key)
        single_connect_nodes_list = [node_obj for node_obj in ordered_nodes_list if len(node_obj.connections) == 1]

file = open('even_trees.txt', 'r')
nodes, edges = file.readline().strip().split()
nodes, edges = int(nodes), int(edges)
nodes = {idx: Node(idx) for idx in range(1, nodes + 1)}
add_connections(nodes, edges)
build_tree(sorted(nodes.values()), nodes)

trees = [Tree(node.key) for node in nodes if len(node.children) == 0]
loose_nodes = len(nodes) - len(leaves)
while loose_nodes > 0:
    for tree in trees:
