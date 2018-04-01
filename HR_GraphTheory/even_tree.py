from collections import defaultdict


# classes
class Node:
    def __init__(self, key):
        self.key = key
        self.connections = []
        self.tree = None

    def add_connection(self, node_idx):
        self.connections.append(node_idx)

    def __lt__(self, other):
        if len(self.connections) == len(other.connections):
            return self.key < other.key
        else:
            return len(self.connections) < len(other.connections)


class Tree:
    def __init__(self, key):
        self.nodes = set()
        self.connected_nodes = set()
        self.key = key
        self.active = True

    def __init__(self, start_node, key):
        self.nodes = set([start_node.key])
        self.connected_nodes = set(start_node.connections)
        self.key = key
        start_node.tree = key
        self.active = True

    def add_node(self, node):
        self.nodes.add(node.key)
        node.tree = self.key
        self.connected_nodes.add(node.connections - self.nodes)

    def size(self):
        return len(self.nodes)

    def __lt__(self, other):
        return len(self.connected_nodes) < len(other.connected_nodes)

    def is_complete(self):
        return len(self.nodes) % 2 == 0


# builders
def add_connections(nodes_obj, num_edges):
    for i in range(num_edges):
        node1, node2 = file.readline().strip().split()
        node1, node2 = int(node1), int(node2)
        nodes_obj[node1].add_connection(node2)
        nodes_obj[node2].add_connection(node1)


# utilities
def merge_trees(tree_idx1, tree_idx2, trees_dict):
    trees_dict[tree_idx1].nodes.update(trees_dict[tree_idx2].nodes)
    for node_obj in trees_dict[tree_idx2].nodes:
        node_obj.tree = tree_idx1
    trees_dict[tree_idx2].active = False


def add_node_to_tree(trees_dict, tree_idx, node_obj):
    trees_dict[tree_idx].add_node(node_obj)
    node_obj.tree = tree_idx


# process
file = open('even_trees.txt', 'r')
nodes, edges = file.readline().strip().split()
nodes, edges = int(nodes), int(edges)
nodes = {idx: Node(idx) for idx in range(1, nodes + 1)}
add_connections(nodes, edges)

sorted_nodes = sorted(nodes.values())
trees = {idx: Tree(node, idx) for idx, node in enumerate(sorted_nodes) if len(node.connections) == 1}
loose_nodes = [node for node in sorted_nodes if len(node.connections) > 1]

while len(loose_nodes) > 0:

    for tree in trees:
        if tree.active:
            if tree.is_complete():
                for connection in tree.connected_nodes:
                    connection_tree = nodes[connection].tree
                    if (not connection_tree is None) and (not trees[connection_tree].is_complete()):
                        merge_trees(trees[connection_tree].key, tree.key,)
            





















#
#
# def get_initial_trees(nodes_obj):
#     #only get trees for leaves!
#     return [Tree(node) for node in nodes_obj.values()]
#
#
# def get_leaves(nodes_obj):
#     return set([node for node in nodes_obj if len(node.connections)==1])
#
#
# tree_ends = get_leaves(nodes.values())
# tree_sizes = defaultdict(int)
# nodes_without_trees = len(nodes.items())
# odd_trees = 0
#
# for idx, leaf in enumerate(tree_ends):
#     leaf.tree = idx
#     tree_sizes.append[1]
#     nodes_without_trees -= 1
#     odd_trees += 1
#
# while nodes_without_trees > 0 or odd_trees > 0:
#     for node in tree_ends:
#         if tree_sizes[node.tree] % 2 == 1:
#
#
#
#
# trees = get_initial_trees(nodes)
# trees.sort()
#
# a = 1
