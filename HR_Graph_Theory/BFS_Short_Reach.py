import sys
import math


class Node:
    __slots__ = ['distance', 'connections']

    def __init__(self):
        self.distance = math.inf
        self.connections = []


def perform_bfs(graph, starting_node):
    unsearched_nodes = list(range(1, len(graph)+1))
    node_queue = [starting_node]
    unsearched_nodes.remove(starting_node)
    graph[starting_node].distance = 0
    while len(node_queue) > 0:
        current_node_index = node_queue.pop(0)
        current_node = graph[current_node_index]
        for child_node_index in current_node.connections:
            child_node = graph[child_node_index]
            child_node.distance = min(child_node.distance, current_node.distance + 1)
            if child_node_index in unsearched_nodes:
                node_queue.append(child_node_index)
                unsearched_nodes.remove(child_node_index)



# q = int(input().strip())
file = open('BFS_Short_Reach.txt', 'r')
q = int(file.readline().strip())
for query in range(q):
    # num_nodes, num_edges = input().strip().split(' ')
    num_nodes, num_edges = file.readline().strip().split(' ')
    num_nodes, num_edges = [int(num_nodes), int(num_edges)]
    nodes = [Node() for i in range(num_nodes+1)] #creating an extra dummy node to allow for indexing from 1

    for edge in range(num_edges):
        # node_1, node_2 = input().strip().split(' ')
        node_1, node_2 = file.readline().strip().split(' ')
        node_1, node_2 = [int(node_1),int(node_2)]
        if node_2 not in nodes[node_1].connections:
            nodes[node_1].connections.append(node_2)
        if node_1 not in nodes[node_2].connections:
            nodes[node_2].connections.append(node_1)

    # starting_node = int(input().strip())
    starting_node = int(file.readline().strip())

    perform_bfs(nodes, starting_node)

    string_rep = ''
    for index, node in enumerate(nodes):
        if index != starting_node and index > 0:
            string_rep += str(6*node.distance if node.distance != math.inf else -1) + ' '
    print(string_rep)