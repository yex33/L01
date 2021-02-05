import timeit
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np

from lab3 import (create_random_list, my_quicksort, 
                  create_near_sorted_list)

import sys
sys.setrecursionlimit(2000)

from sorts import (dual_pivot_quicksort, quad_pivot_quicksort,
                   quicksort_inplace, tri_pivot_quicksort,
                   bubble_sort, insertion_sort, selection_sort)


# # in-place version timing experiments
# def run_mult(func, n, n_proc):
#     with Pool(processes=n_proc) as pool:
#         return pool.map(func, n)
#
#
# def ip_vs_ax(n):
#     L = create_random_list(n)
#     L2 = L.copy()
#     qsip = quicksort_inplace
#     qsax = my_quicksort
#     ip = timeit.timeit("qsip(L)", globals=locals(), number=1)
#     ax = timeit.timeit("qsax(L2)", globals=locals(), number=1)
#     return [ip, ax]
#
#
# def ip_exp():
#     n_range = (list(range(10 ** 4, 10 ** 5, 10 ** 4))
#                + list(range(10 ** 5, 10 ** 6, 10 ** 5))
#                + list(range(10 ** 6, 10 ** 7, 10 ** 6)))
#     res = run_mult(ip_vs_ax, n_range, 6)
# 
#     N = np.array(n_range)
#     N_log10 = np.log10(N)
#     res = np.array(res)
#     ip_data = res[:, 0]  # in-place version results
#     ax_data = res[:, 1]  # auxiliary array version results
# 
#     # plotting
#     plt.figure()
#     plt.plot(N_log10, ip_data, "o-", lw=1, ms=3, label="in-place")
#     plt.plot(N_log10, ax_data, "o-", lw=1, ms=3, label="non-in-place")
#     plt.legend()
#     plt.title("Semi-log plot for in-place and non-in-place quicksort")
#     plt.xlabel("$\log_{10}{n}$, array of size $n$")
#     plt.ylabel("Runtime (s)")
#     plt.savefig("images/ip-ax.png", dpi=300)
#     plt.xlim(4, 6)
#     plt.ylim(0, 3)
#     plt.savefig("images/ip-ax-zoomed.png", dpi=300)
#
#     # performance comparison
#     ip_c = ip_data / (N * np.log2(N))
#     ax_c = ax_data / (N * np.log2(N))
#     improvement = int(np.average((ip_c - ax_c) / ax_c) * 100)
#     print(f"Non-in-place is {improvement}% faster than in-place.")
#
#
# def multp_exp():
#     pass
#
#
# # Muti-pivot timing experiments
# n_range = range(100_000, 1_000_000, 10_000)
# quick_res = []  # my_quciksort results
# dual_res = []   # dual_pivot_quicksort results
# tri_res = []    # tri_pivot_quicksort results
# qua_res = []    # quad_pivot_quicksort results
# 
# for n in n_range:
#     L = create_random_list(n)
#     L2 = L.copy()
#     L3 = L.copy()
#     L4 = L.copy()
#     qs1 = my_quicksort
#     qs2 = dual_pivot_quicksort
#     qs3 = tri_pivot_quicksort
#     qs4 = quad_pivot_quicksort
#     one_pivot = timeit.timeit("qs1(L)", globals=globals(), number=1)
#     quick_res.append(one_pivot)
#     two_pivot = timeit.timeit("qs2(L2)", globals=globals(), number=1)
#     dual_res.append(two_pivot)
#     three_pivot = timeit.timeit("qs3(L3)", globals=globals(), number=1)
#     tri_res.append(three_pivot)
#     four_pivot = timeit.timeit("qs4(L4)", globals=globals(), number=1)
#     qua_res.append(four_pivot)
#
# N = np.array(list(n_range))
# qs1_data = np.array(quick_res)
# qs2_data = np.array(dual_res)
# qs3_data = np.array(tri_res)
# qs4_data = np.array(qua_res)
#
# # plotting for muti-poivt
# plt.figure()
# plt.plot(N, qs1_data, color='black', linewidth=0.5, label="my_quicksort")
# plt.plot(N, qs2_data, color='green', linewidth=0.5, label="dual_pivot")
# plt.plot(N, qs3_data, color='blue', linewidth=0.5, label="tri_pivot")
# plt.plot(N, qs4_data, color='red', linewidth=0.5, label="quad_pivot")
# plt.legend()
# plt.show()


# # Compare worst case with average case of quicksort
n_range = range(10, 1_000, 10)
worst_res = []    # worst case results
average_res = []  # average case results

for n in n_range:
    L = create_random_list(n)
    qs = quad_pivot_quicksort
    average_time = timeit.timeit("qs(L)", globals=globals(), number=1)
    average_res.append(average_time)
    worst_time = timeit.timeit("qs(L)", globals=globals(), number=1)
    worst_res.append(worst_time)

N = np.array(list(n_range))
average_data = np.array(average_res)
worst_data = np.array(worst_res)

# plotting for worst case vs average case
plt.figure()
plt.plot(N, average_data, color='blue', linewidth=0.5, label="average_case")
plt.plot(N, worst_data, color='red', linewidth=0.5, label="worst_case")
plt.legend()
plt.show()

# Compare quicksort with elementary sorting algorithms
n_range = []
for i in range(0, 100):
    n_range.append(0.01 * i)
qs_res = []   #quicksort results
bub_res = []  #bubble_sort results
sel_res = []  #selection_sort results
ins_res = []  #insertion_sort results

for n in n_range:
    L = create_near_sorted_list(1000, n)
    L2 = L.copy()
    L3 = L.copy()
    L4 = L.copy()
    qs = quad_pivot_quicksort
    bub = bubble_sort
    sel = selection_sort
    ins = insertion_sort
    qs_time = timeit.timeit("qs(L)", globals=globals(), number=1)
    qs_res.append(qs_time)
    bub_time = timeit.timeit("bub(L2)", globals=globals(), number=1)
    bub_res.append(bub_time)
    sel_time = timeit.timeit("sel(L3)", globals=globals(), number=1)
    sel_res.append(sel_time)
    ins_time = timeit.timeit("ins(L4)", globals=globals(), number=1)
    ins_res.append(ins_time) 
    
N = np.array(list(n_range))
qs_data = np.array(qs_res)
bub_data = np.array(bub_res)
sel_data = np.array(sel_res)
ins_data = np.array(ins_res)

#plotting for quicksort vs elementary sorting algorithms
plt.figure()
plt.plot(N, qs_data, color='black', linewidth=0.5, label="quicksort")
plt.plot(N, bub_data, color='green', linewidth=0.5, label="bubble_sort")
plt.plot(N, sel_data, color='blue', linewidth=0.5, label="selection_sort")
plt.plot(N, ins_data, color='red', linewidth=0.5, label="insertion_sort")
plt.legend()
plt.show()

# # Compare quicksort with elementary sorting methods
# n_range = range(1, 20, 1)
# qui_res = []  # quicksort_inplace results
# bub_res = []  # bubblesort results
# sel_res = []  # selection results
# ins_res = []  # insertion results
# for n in n_range:
#     L = create_random_list(n)
#     L2 = L.copy()
#     L3 = L.copy()
#     L4 = L.copy()
#     qui = quicksort_inplace
#     bub = bubble_sort
#     sel = selection_sort
#     ins = insertion_sort
#     qui_time = min(timeit.repeat("qui(L)", globals=globals(), repeat=5, number=100))
#     qui_res.append(qui_time)
#     bub_time = min(timeit.repeat("bub(L)", globals=globals(), repeat=5, number=100))
#     bub_res.append(bub_time)
#     sel_time = min(timeit.repeat("sel(L)", globals=globals(), repeat=5, number=100))
#     sel_res.append(sel_time)
#     ins_time = min(timeit.repeat("ins(L)", globals=globals(), repeat=5, number=100))
#     ins_res.append(ins_time)
#
# N = np.array(list(n_range))
# qui_data = np.array(qui_res)
# bub_data = np.array(bub_res)
# sel_data = np.array(sel_res)
# ins_data = np.array(ins_res)
#
# # plotting for muti-poivt
# plt.figure()
# plt.plot(N, qui_data, color='black', linewidth=0.5, label="quicksort_inplace")
# plt.plot(N, bub_data, color='green', linewidth=0.5, label="bubble_sort")
# plt.plot(N, sel_data, color='blue', linewidth=0.5, label="selection_sort")
# plt.plot(N, ins_data, color='red', linewidth=0.5, label="insertion_sort")
# plt.legend()
# plt.show()
#
#
# if __name__ == "__main__":
#     ip_exp()
#     multp_exp()
