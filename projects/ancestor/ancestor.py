import sys
sys.path.append('../graph')
from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for tup in ancestors:
        if tup[0] not in g.vertices:
            g.add_vertex(tup[0])
        if tup[1] not in g.vertices:
            g.add_vertex(tup[1])

    for vert in ancestors:
        g.add_edge(vert[1], vert[0])

    if g.vertices[starting_node] == set():
        return -1

    return g.bft(starting_node)

    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))