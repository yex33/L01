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
    n_range = list(range(10 ** 1, 10 ** 3))
    build1_res = []
    build2_res = []
    build3_res = []

    for n in n_range:
        L = create_random_list(n)
        setup = "from heap import Heap;h = Heap([]);h.data = L.copy()"
        bh1_time = min(timeit.repeat("h.build_heap1()", setup, globals=locals(), repeat=10, number=1))
        build1_res.append(bh1_time)
        bh2_time = min(timeit.repeat("h.build_heap2()", setup, globals=locals(), repeat=10, number=1))
        build2_res.append(bh2_time)
        bh3_time = min(timeit.repeat("h.build_heap3()", setup, globals=locals(), repeat=10, number=1))
        build3_res.append(bh3_time)

    N = np.array(n_range)
    bh1_data = np.array(build1_res)
    bh2_data = np.array(build2_res)
    bh3_data = np.array(build3_res)

    # plotting for build_heap 1 2 and 3
    plt.figure()
    plt.scatter(N, bh1_data, color="blue", s=0.3, label="build heap1")
    plt.scatter(N, bh2_data, color="black", s=0.3, label="build heap2")
    plt.scatter(N, bh3_data, color="red", s=0.3, label="build heap3")
    plt.title("Run time of three algorithms for building heaps")
    plt.xlabel("$n$, heap size")
    plt.ylabel("Run time (s)")
    plt.legend()
    plt.savefig("images/heap-comparison.png", dpi=300)

    # linear regression for 1
    a, b = np.polyfit(N, bh1_data, 1)
    x = N
    y = a * x + b
    rsq = np.corrcoef(bh1_data, y)[0, 1] ** 2
    plt.figure()
    plt.scatter(N, bh1_data, s=0.3, label="build heap1")
    plt.plot(x, y, lw=0.5, color="red", label="Regression")
    plt.title("Linear regression on build heap1")
    plt.xlabel("$n$, heap size")
    plt.ylabel("Run time (s)")
    equation_text = f"$y = ({a:.4g})x + ({b:.4g})$\n$R^2 = {rsq:.4g}$"
    plt.annotate(equation_text, xy=(x[5], y[-5]))
    plt.legend()
    plt.savefig("images/build1.png", dpi=300)

    # linear regression for 2
    a, b = np.polyfit(N, bh2_data, 1)
    x = N
    y = a * x + b
    rsq = np.corrcoef(bh2_data, y)[0, 1] ** 2
    plt.figure()
    plt.scatter(N, bh2_data, s=0.3, label="build heap2")
    plt.plot(x, y, lw=0.5, color="red", label="Regression")
    plt.title("Linear regression on build heap2")
    plt.xlabel("$n$, heap size")
    plt.ylabel("Run time (s)")
    equation_text = f"$y = ({a:.4g})x + ({b:.4g})$\n$R^2 = {rsq:.4g}$"
    plt.annotate(equation_text, xy=(x[5], y[2 * len(y) // 3]))
    plt.legend()
    plt.savefig("images/build2.png", dpi=300)

    # linear regression for 3
    a, b, c = np.polyfit(np.log(N), bh3_data, 2)
    x = N
    y = a * np.log(x) ** 2 + b * np.log(x) + c
    rsq = np.corrcoef(bh3_data, y)[0, 1] ** 2
    plt.figure()
    plt.scatter(N, bh3_data, s=0.3, label="build heap3")
    plt.plot(x, y, lw=0.5, color="red", label="Regression")
    plt.title("Linear regression on build heap3")
    plt.xlabel("$n$, heap size")
    plt.ylabel("Run time (s)")
    equation_text = f"$y = ({a:.4g})(\ln x)^2 + ({b:.4g})\ln x + ({c:.4g})$\n$R^2 = {rsq:.4g}$"
    plt.annotate(equation_text, xy=(x[5], y[2 * len(y) // 3]))
    plt.legend()
    plt.savefig("images/build3.png", dpi=300)


if __name__ == "__main__":
    build_heap_test()
