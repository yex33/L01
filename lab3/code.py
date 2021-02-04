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
    n_range = (list(range(10 ** 4, 10 ** 5, 10 ** 4))
               + list(range(10 ** 5, 10 ** 6, 10 ** 5))
               + list(range(10 ** 6, 10 ** 7, 10 ** 6)))
    res = run_mult(ip_vs_ax, n_range, 6)

    N = np.array(n_range)
    N_log10 = np.log10(N)
    res = np.array(res)
    ip_data = res[:, 0]  # in-place version results
    ax_data = res[:, 1]  # auxiliary array version results

    # plotting
    plt.figure()
    plt.plot(N_log10, ip_data, "o-", lw=1, ms=3, label="in-place")
    plt.plot(N_log10, ax_data, "o-", lw=1, ms=3, label="non-in-place")
    plt.legend()
    plt.title("Semi-log plot for in-place and non-in-place quicksort")
    plt.xlabel("$\log_{10}{n}$, array of size $n$")
    plt.ylabel("Runtime (s)")
    plt.savefig("images/ip-ax.png", dpi=300)
    plt.xlim(4, 6)
    plt.ylim(0, 3)
    plt.savefig("images/ip-ax-zoomed.png", dpi=300)

    # performance comparison
    ip_c = ip_data / (N * np.log2(N))
    ax_c = ax_data / (N * np.log2(N))
    improvement = int(np.average((ip_c - ax_c) / ax_c) * 100)
    print(f"Non-in-place is {improvement}% faster than in-place.")


def multp_exp():
    pass


if __name__ == "__main__":
    ip_exp()
    multp_exp()
