import random
import timeit

import matplotlib.pyplot as plt
import numpy as np

from heap import Heap


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1, n))
    return L


# build_heap(1, 2, and 3) timing test
def Build_heap_test():
    n_range = range(10, 1_000, 10)
    build1_res = []
    build2_res = []
    build3_res = []

    for n in n_range:
        L = create_random_list(n)
        heap = Heap([])
        bh1_time = timeit.timeit("heap.build_heap1()", "heap.data = L.copy()", globals=locals(), number=1)
        build1_res.append(bh1_time)
        bh2_time = timeit.timeit("heap.build_heap2()", "heap.data = L.copy()", globals=locals(), number=1)
        build2_res.append(bh2_time)
        bh3_time = timeit.timeit("heap.build_heap3()", "heap.data = L.copy()", globals=locals(), number=1)

    N = np.array(list(n_range))
    bh1_data = np.array(build1_res)
    bh2_data = np.array(build2_res)
    bh3_data = np.array(build3_res)

    # plotting for build_heap 1 2 and 3
    plt.figure()
    plt.plot(N, bh1_data, color="blue", linewidth=1, label="build_heap1")
    plt.plot(N, bh2_data, color="black", linewidth=1, label="build_heap2")
    plt.plot(N, bh3_data, color="red", linewidth=1, label="build_heap3")
    plt.title("Run time of three build_heap")
    plt.xlabel("$n$, heap size")
    plt.ylabel("Run time (s)")


Build_heap_test()

