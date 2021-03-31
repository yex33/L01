import timeit
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
from numpy.core.numeric import correlate

from lab9 import *
from shortest_paths import *

rc("font", **{"family": "serif", "size": 12})
rc("text", usetex=True)

timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

N = 100
W = 1000

def correct():
    G = create_random_complete_graph(10, 100)
    source = list(G.adj.keys())[0]
    print(bellman_ford(G, source))
    print(bellman_ford_approx(G, source, 5))
    print(bellman_ford_approx2(G, source, 5))

    dij = all_pairs_dijkstra(G)
    bel = all_pairs_bellman_ford(G)
    floyd = mystery(G)
    print(dij)
    print(bel)
    print(floyd)
    print(dij == bel == floyd)


def run_mult(func, n, n_proc):
    with Pool(processes=n_proc) as pool:
        return pool.map(func, n)


def acc_vs_approx(k):
    G = create_random_complete_graph(N, W)
    source = list(G.adj.keys())[0]
    setup = "from lab9 import bellman_ford; from shortest_paths import bellman_ford_approx, bellman_ford_approx2"
    acc_rt, acc_dist = timeit.timeit("acc_dist = bellman_ford(G, source)", setup, globals=locals(), number=1)
    approx_rt, approx_dist = timeit.timeit("approx_dist = bellman_ford_approx(G, source, k)", setup, globals=locals(), number=1)
    approx2_rt, _ = timeit.timeit("approx_dist = bellman_ford_approx2(G, source, k)", setup, globals=locals(), number=1)
    return acc_rt, total_dist(acc_dist), approx_rt, total_dist(approx_dist), approx2_rt


def comp():
    ks = np.arange(1, 25 + 1)
    res = run_mult(acc_vs_approx, ks, 6)
    res = np.array(res)
    acc_rt = res[:, 0]
    acc_td = res[:, 1]
    approx_rt = res[:, 2]
    approx_td = res[:, 3]
    approx2_rt = res[:, 4]

    ax = plt.figure().gca()
    plt.scatter(ks, acc_rt, s=5, label="Original")
    plt.scatter(ks, approx_rt, s=5, label="Approximation")
    plt.scatter(ks, approx2_rt, s=5, label="Approx. Optimization Attempt")
    plt.legend()
    plt.title("Run time of the original and the approximate implementation")
    plt.xlabel("$k$")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel("Run time (s)")
    plt.savefig("images/rtcomp.png", dpi=300)

    ax = plt.figure().gca()
    plt.plot(ks, acc_td, lw=1, label="Original")
    plt.plot(ks, approx_td, lw=1, label="Approximation")
    plt.legend()
    plt.title("Total distance from source computed by two implementations")
    plt.xlabel("$k$")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.ylabel("Total Distance")
    plt.savefig("images/tdcomp.png", dpi=300)


if __name__ == "__main__":
    correct()
    comp()

