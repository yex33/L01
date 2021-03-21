from lab8 import WeightedGraph
from mst import prim1

graph = WeightedGraph(10)
edges = [
    (0, 1, 3),
    (0, 2, 6),
    (0, 4, 9),
    (1, 2, 4),
    (1, 3, 2),
    (1, 5, 9),
    (1, 4, 9),
    (2, 6, 9),
    (2, 3, 2),
    (3, 6, 9),
    (3, 5, 8),
    (4, 5, 8),
    (4, 9, 18),
    (5, 6, 7),
    (5, 8, 9),
    (5, 9, 10),
    (6, 7, 4),
    (6, 8, 5),
    (7, 8, 1),
    (7, 9, 4),
    (8, 9, 3),
]
for edge in edges:
    graph.add_edge(*edge)
print(prim1(graph).adj)
