from collections import deque
from multiprocessing import Pool
from random import randrange
from timeit import timeit

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from numpy.lib.function_base import insert

from lab8 import WeightedGraph
from mst import prim1, prim2

rc("font", **{"family": "serif", "size": 12})
rc("text", usetex=True)

def is_connected(graph: WeightedGraph):
    source = list(graph.adj.keys())[0]
    queue = deque([source])
    marked = {node: False for node in graph.adj.keys()}
    marked[source] = True
    count = 1
    while len(queue) != 0:
        cur = queue.popleft()
        for node in graph.adjacent_nodes(cur):
            if not marked[node[0]]:
                count += 1
                queue.append(node[0])
                marked[node[0]] = True
    return count == graph.number_of_nodes()


def connected_graph(n: int) -> WeightedGraph:
    graph = WeightedGraph(n)
    for _ in range(2 * n):
        graph.add_edge(randrange(n), randrange(n), randrange(10 * n))
    while not is_connected(graph):
        for _ in range(n // 10):
            graph.add_edge(randrange(n), randrange(n), randrange(10 * n))
    return graph


def test_correct():
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
    print(prim2(graph).adj)
    print(is_connected(graph))


def run_mult(func, n, n_proc):
    with Pool(processes=n_proc) as pool:
        return pool.map(func, n)


def p1vsp2(n):
    graph = connected_graph(n)
    setup = "from mst import prim1, prim2"
    p1 = timeit("prim1(graph)", setup, globals=locals(), number=1)
    p2 = timeit("prim2(graph)", setup, globals=locals(), number=1)
    return p1, p2


def comp():
    ns = np.arange(100, 1000 + 1, 5)
    res = run_mult(p1vsp2, ns, 6)
    res = np.array(res)
    p1 = res[:, 0]
    p2 = res[:, 1]

    plt.figure()
    plt.scatter(ns, p1, s=1, color="#1f77b4", label="prim1")
    plt.scatter(ns, p2, s=1, color="#ff7f0e", label="prim2")
    plt.legend()
    plt.title("Empirical run time of two versions of Prim's algorithm")
    plt.xlabel("$n$, Number of Vertices")
    plt.ylabel("Run Time (s)")
    plt.savefig("images/comp.png", dpi=300)

    ns_log = np.log(ns)
    p1_log = np.log(p1)
    a, b, *_ = np.polyfit(ns_log, p1_log, 1)
    y = a * ns_log + b
    rsq = np.corrcoef(p1_log, y)[0, 1] ** 2
    equation_text = f"$y = ({a:.4g})x + ({b:.4g})$\n$R^2 = {rsq:.4g}$"
    plt.figure()
    plt.scatter(ns_log, p1_log, s=1, color="#1f77b4")
    plt.plot(ns_log, y, lw=1, color="b")
    plt.title("Empirical run time of Prim v1 (log-log)")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Run Time")
    plt.annotate(equation_text, xy=(ns_log[5], y[-30]))
    plt.savefig("images/v1log.png", dpi=300)

    plt.figure()
    plt.scatter(ns, p2, s=1, color="#ff7f0e")
    plt.title("Empirical run time of Prim v2")
    plt.xlabel("$n$, Number of Vertices")
    plt.ylabel("Run time (s)")
    plt.savefig("images/v2.png", dpi=300)

    plt.figure()
    plt.scatter(ns, p2 / ns, s=1, color="#ff7f0e")
    plt.title("Empirical run time of Prim v2 normalized by $n$")
    plt.xlabel("$n$, Number of Vertices")
    plt.ylabel("Run time (s)")
    plt.savefig("images/v2norm.png", dpi=300)


if __name__ == "__main__":
    comp()
