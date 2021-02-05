import sys
import timeit
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np

from lab3 import create_near_sorted_list, create_random_list, my_quicksort
from sorts import (bubble_sort, dual_pivot_quicksort, insertion_sort,
                   quad_pivot_quicksort, quicksort_inplace, selection_sort,
                   tri_pivot_quicksort)

sys.setrecursionlimit(2000)


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


# Muti-pivot timing experiments
def multp(n):
    L = create_random_list(n)
    L2 = L.copy()
    L3 = L.copy()
    L4 = L.copy()
    qs1 = my_quicksort
    qs2 = dual_pivot_quicksort
    qs3 = tri_pivot_quicksort
    qs4 = quad_pivot_quicksort
    one_pivot = timeit.timeit("qs1(L)", globals=locals(), number=1)
    two_pivot = timeit.timeit("qs2(L2)", globals=locals(), number=1)
    three_pivot = timeit.timeit("qs3(L3)", globals=locals(), number=1)
    four_pivot = timeit.timeit("qs4(L4)", globals=locals(), number=1)
    return [one_pivot, two_pivot, three_pivot, four_pivot]


def multp_exp():
    n_range = (list(range(10 ** 4, 10 ** 5, 10 ** 4))
               + list(range(10 ** 5, 10 ** 6, 10 ** 5))
               + list(range(10 ** 6, 10 ** 7, 10 ** 6)))
    res = run_mult(multp, n_range, 6)

    N = np.array(n_range)
    N_log10 = np.log10(N)
    res = np.array(res)
    qs1_data = res[:, 0]
    qs2_data = res[:, 1]
    qs3_data = res[:, 2]
    qs4_data = res[:, 3]

    # plotting for muti-poivt
    plt.figure()
    plt.plot(N_log10, qs1_data,
             "o-", color="black", lw=1, ms=3, label="my_quicksort")
    plt.plot(N_log10, qs2_data,
             "o-", color="green", lw=1, ms=3, label="dual_pivot")
    plt.plot(N_log10, qs3_data,
             "o-", color="blue", lw=1, ms=3, label="tri_pivot")
    plt.plot(N_log10, qs4_data,
             "o-", color="red", lw=1, ms=3, label="quad_pivot")
    plt.legend()
    plt.title("Semi-log plot for multi-pivots quicksort")
    plt.xlabel("$\log_{10}{n}$, array of size $n$")
    plt.ylabel("Runtime (s)")
    plt.savefig("images/multp.png", dpi=300)
    plt.xlim(4, 6)
    plt.ylim(0, 3)
    plt.savefig("images/multp-zoomed-1.png", dpi=300)
    plt.xlim(4, 5)
    plt.ylim(0, 0.3)
    plt.savefig("images/multp-zoomed-2.png", dpi=300)


# Compare worst case with average case of quicksort
def worst_exp():
    n_range = range(10, 1_000, 10)
    worst_res = []    # worst case results
    average_res = []  # average case results

    for n in n_range:
        L = create_random_list(n)
        qs = quad_pivot_quicksort
        average_time = timeit.timeit("qs(L)", globals=locals(), number=1)
        average_res.append(average_time)
        worst_time = timeit.timeit("qs(L)", globals=locals(), number=1)
        worst_res.append(worst_time)

    N = np.array(list(n_range))
    average_data = np.array(average_res)
    worst_data = np.array(worst_res)

    # plotting for worst case vs average case
    plt.figure()
    plt.plot(N, average_data, color="blue", linewidth=1, label="average case")
    plt.plot(N, worst_data, color="red", linewidth=1, label="worst case")
    plt.title("Quad-pivot quicksort in average and in worst case")
    plt.xlabel("$n$, array size")
    plt.ylabel("Runtime (s)")
    plt.legend()
    plt.savefig("images/worst.png", dpi=300)

    # Compare quicksort with elementary sorting algorithms
    n_range = range(0, 100)
    qs_res = []   # quicksort results
    bub_res = []  # bubble_sort results
    sel_res = []  # selection_sort results
    ins_res = []  # insertion_sort results

    for n in n_range:
        L = create_near_sorted_list(1000, n / 100)
        L2 = L.copy()
        L3 = L.copy()
        L4 = L.copy()
        qs = quad_pivot_quicksort
        bub = bubble_sort
        sel = selection_sort
        ins = insertion_sort
        qs_time = timeit.timeit("qs(L)", globals=locals(), number=1)
        qs_res.append(qs_time)
        bub_time = timeit.timeit("bub(L2)", globals=locals(), number=1)
        bub_res.append(bub_time)
        sel_time = timeit.timeit("sel(L3)", globals=locals(), number=1)
        sel_res.append(sel_time)
        ins_time = timeit.timeit("ins(L4)", globals=locals(), number=1)
        ins_res.append(ins_time)

    N = np.array(list(n_range))
    qs_data = np.array(qs_res)
    bub_data = np.array(bub_res)
    sel_data = np.array(sel_res)
    ins_data = np.array(ins_res)

    # plotting for quicksort vs elementary sorting algorithms
    plt.figure()
    plt.plot(N, qs_data, color="black", linewidth=1, label="quicksort")
    plt.plot(N, bub_data, color="green", linewidth=1, label="bubble sort")
    plt.plot(N, sel_data, color="blue", linewidth=1, label="selection sort")
    plt.plot(N, ins_data, color="red", linewidth=1, label="insertion sort")
    plt.title("Quad-pivot quicksort and elementary sorts on near-sorted-lists")
    plt.xlabel("Sorted Factor (%)")
    plt.ylabel("Runtime (s)")
    plt.legend()
    plt.savefig("images/near-sorted.png", dpi=300)


# Compare quicksort with elementary sorting methods on small lists
def small_exp():
    n_range = range(1, 20, 1)
    qui_res = []  # quicksort_inplace results
    bub_res = []  # bubblesort results
    sel_res = []  # selection results
    ins_res = []  # insertion results
    for n in n_range:
        L = create_random_list(n)
        qui = quicksort_inplace
        bub = bubble_sort
        sel = selection_sort
        ins = insertion_sort
        setup = "L1 = L.copy()"
        qui_time = sum(timeit.repeat("qui(L1)", setup=setup,
                                     globals=locals(), repeat=100, number=1))
        qui_res.append(qui_time)
        bub_time = sum(timeit.repeat("bub(L1)", setup=setup,
                                     globals=locals(), repeat=100, number=1))
        bub_res.append(bub_time)
        sel_time = sum(timeit.repeat("sel(L1)", setup=setup,
                                     globals=locals(), repeat=100, number=1))
        sel_res.append(sel_time)
        ins_time = sum(timeit.repeat("ins(L1)", setup=setup,
                                     globals=locals(), repeat=100, number=1))
        ins_res.append(ins_time)

    N = np.array(list(n_range))
    qui_data = np.array(qui_res)
    bub_data = np.array(bub_res)
    sel_data = np.array(sel_res)
    ins_data = np.array(ins_res)

    # plotting for muti-poivt
    plt.figure()
    plt.plot(N, qui_data, color="black", lw=1, label="quicksort_inplace")
    plt.plot(N, bub_data, color="green", lw=1, label="bubble_sort")
    plt.plot(N, sel_data, color="blue", lw=1, label="selection_sort")
    plt.plot(N, ins_data, color="red", lw=1, label="insertion_sort")
    plt.legend()
    plt.title("Runtime of elementary sorts on small lists")
    plt.xlabel("$n$, array size")
    plt.ylabel("Runtime (s)")
    plt.savefig("images/small.png", dpi=300)


if __name__ == "__main__":
    # ip_exp()
    # multp_exp()
    worst_exp()
    # small_exp()
