import timeit
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np

from lab3 import create_random_list, my_quicksort
from sorts import quicksort_inplace


# in-place version timing experiments
def run_mult(func, n, n_proc):
    with Pool(processes=n_proc) as pool:
        return pool.map(func, n)


def ip_vs_ax(n):
    L = create_random_list(n)
    L2 = L.copy()
    qsip = quicksort_inplace
    qsax = my_quicksort
    ip = timeit.timeit("qsip(L)", globals=locals(), number=1)
    ax = timeit.timeit("qsax(L2)", globals=locals(), number=1)
    return [ip, ax]


def ip_exp():
    n_range = list(range(100, 100_000, 100))
    res = run_mult(ip_vs_ax, n_range, 8)

    N = np.array(n_range)
    res = np.array(res)
    ip_data = res[:, 0]  # in-place version results
    ax_data = res[:, 1]  # auxiliary array version results

    # plotting
    plt.figure()
    plt.scatter(N, ip_data, s=0.5, label="in-place")
    plt.scatter(N, ax_data, s=0.5, label="auxiliary")
    plt.legend()
    plt.savefig("images/ip-ax.png", dpi=300)

    # performance comparison
    ip_c = ip_data / (N * np.log2(N))
    ax_c = ax_data / (N * np.log2(N))
    improvement = int(np.average((ip_c - ax_c) / ax_c) * 100)
    print(f"Auxiliary is {improvement}% faster than in-place.")


def multp_exp():
    pass


if __name__ == "__main__":
    # ip_exp()
    multp_exp()
