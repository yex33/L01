from random import randrange

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc("font", **{"family": "serif", "size": 12})
rc("text", usetex=True)

from graphs import *
from lab7 import Graph

# graph = Graph(9)
# # graph.add_edge(1, 2)
# graph.add_edge(1, 3)
# graph.add_edge(2, 4)
# graph.add_edge(3, 4)
# graph.add_edge(3, 5)
# graph.add_edge(5, 7)
# # graph.add_edge(7, 8)
# graph.add_edge(5, 8)
# # graph.add_edge(4, 5)
# graph.add_edge(4, 6)
# # graph.add_edge(5, 6)
# 
# print(BFS2(graph, 1, 2))
# print(DFS2(graph, 1, 2))
# 
# print(BFS3(graph, 1))
# print(DFS3(graph, 1))
# 
# print(has_cycle(graph))


K = 100
C = 300
N = 10


def graph_test(c: int, k: int, f) -> bool:
    g: Graph = Graph(k)
    for _ in range(c):
        g.add_edge(randrange(k), randrange(k))
    return f(g)

def cycle_vs_c():
    portions = []
    cs = np.arange(1, C + 1, 2)
    for c in cs:
        portions.append(sum(graph_test(c, K, has_cycle) for _ in range(N)) / N)
    portions = np.array(portions)
    plt.figure()
    plt.scatter(cs, portions * 100, s=1)
    plt.title("Portions of graphs which have a cycle with $c$ random edges")
    plt.xlabel("$c$, Number of Edges Added")
    plt.ylabel("Portion of Cyclic Graphs (\%)")
    plt.savefig("images/cyclic.png", dpi=300)

def connected_vs_c():
    portions = []
    cs = np.arange(1, C + 1, 2)
    for c in cs:
        portions.append(sum(graph_test(c, K, is_connected) for _ in range(N)) / N)
    portions = np.array(portions)
    plt.figure()
    plt.scatter(cs, portions * 100, s=1)
    plt.title("Portions of graphs which is connected with $c$ random edges")
    plt.xlabel("$c$, Number of Edges Added")
    plt.ylabel("Portion of Connected Graphs (\%)")
    plt.savefig("images/connect.png", dpi=300)

if __name__ == "__main__":
    cycle_vs_c()
    connected_vs_c()
