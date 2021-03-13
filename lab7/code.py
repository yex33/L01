from graphs import BFS3, DFS2, DFS3, has_cycle, has_cycle_bfs
from lab7 import Graph

graph = Graph(7)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
# graph.add_edge(2, 4)
# graph.add_edge(3, 4)
# graph.add_edge(3, 5)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)

print(DFS2(graph, 1, 1))

print(BFS3(graph, 1))
print(DFS3(graph, 1))

print(has_cycle_bfs(graph))
print(has_cycle(graph))
