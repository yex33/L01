import random
import timeit

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

from heap import Heap

rc("font", **{"family": "serif", "size": 12})
rc("text", usetex=True)

def create_random_list(n):
    return [random.randint(1, 2 * n) for _ in range(n)]

# build_heap(1, 2, and 3) timing test
def build_heap_test():
    n_range = (list(range(10 ** 4, 10 ** 5, 10 ** 4)))
               # + list(range(10 ** 5, 10 ** 6, 10 ** 5))
               # + list(range(10 ** 6, 10 ** 7, 10 ** 6)))
    build1_res = []
    build2_res = []
    build3_res = []

    for n in n_range:
        L = create_random_list(n)
        heap = Heap([])
        setup = "heap.data = L.copy()"
        bh1_time = timeit.timeit("heap.build_heap1()", setup, globals=locals(), number=1)
        build1_res.append(bh1_time)
        bh2_time = timeit.timeit("heap.build_heap2()", setup, globals=locals(), number=1)
        build2_res.append(bh2_time)
        bh3_time = timeit.timeit("heap.build_heap3()", setup, globals=locals(), number=1)
        build3_res.append(bh3_time)

    N = np.array(n_range)
    bh1_data = np.array(build1_res)
    bh2_data = np.array(build2_res)
    bh3_data = np.array(build3_res)

    # plotting for build_heap 1 2 and 3
    plt.figure()
    plt.plot(N, bh1_data, color="blue", linewidth=1, label="build heap1")
    plt.plot(N, bh2_data, color="black", linewidth=1, label="build heap2")
    plt.plot(N, bh3_data, color="red", linewidth=1, label="build heap3")
    plt.title("Run time of three algorithms for building heaps")
    plt.xlabel("$n$, heap size")
    plt.ylabel("Run time (s)")
    plt.legend()
    plt.savefig("images/heap-comparison.png", dpi=300)


if __name__ == "__main__":
    build_heap_test()
