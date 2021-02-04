import timeit
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np

from lab3 import create_random_list, my_quicksort
from sorts import (dual_pivot_quicksort, quad_pivot_quicksort,
                   quicksort_inplace, tri_pivot_quicksort)


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


# Muti-pivot timing experiments
n_range = range(1000, 100_000, 1000)
quick_res = []  # my_quciksort results
dual_res = []   # dual_pivot_quicksort results
tri_res = []    # tri_pivot_quicksort results
qua_res = []    # quad_pivot_quicksort results

for n in n_range:
    L = create_random_list(n)
    L2 = L.copy()
    L3 = L.copy()
    L4 = L.copy()
    qs1 = my_quicksort
    qs2 = dual_pivot_quicksort
    qs3 = tri_pivot_quicksort
    qs4 = quad_pivot_quicksort
    one_pivot = timeit.timeit("qs1(L)", globals=globals(), number=1)
    quick_res.append(one_pivot)
    two_pivot = timeit.timeit("qs2(L2)", globals=globals(), number=1)
    dual_res.append(two_pivot)
    three_pivot = timeit.timeit("qs3(L3)", globals=globals(), number=1)
    tri_res.append(three_pivot)
    four_pivot = timeit.timeit("qs4(L4)", globals=globals(), number=1)
    qua_res.append(four_pivot)

N = np.array(list(n_range))
qs1_data = np.array(quick_res)
qs2_data = np.array(dual_res)
qs3_data = np.array(tri_res)
qs4_data = np.array(qua_res)

# plotting for muti-poivt
plt.figure()
plt.plot(N, qs1_data, color='black', linewidth=0.5, label="my_quicksort")
plt.plot(N, qs2_data, color='green', linewidth=0.5, label="dual_pivot")
plt.plot(N, qs3_data, color='blue', linewidth=0.5, label="tri_pivot")
plt.plot(N, qs4_data, color='red', linewidth=0.5, label="quad_pivot")
plt.legend()
plt.show()


if __name__ == "__main__":
    ip_exp()
    multp_exp()
