import timeit

import matplotlib.pyplot as plt
import numpy as np

from lab3 import create_random_list, my_quicksort
from sorts import dual_pivot_quicksort, tri_pivot_quicksort, quad_pivot_quicksort


# in-place version timing experiments
# n_range = range(1000, 100_000, 1000)
# ip_res = []  # in-place version results
# ax_res = []  # auxiliary array version results
# for n in n_range:
#     L = create_random_list(n)
#     L2 = L.copy()
#     qsip = quicksort_inplace
#     qsax = my_quicksort
#     ip = timeit.timeit("qsip(L)", globals=globals(), number=1)
#     ip_res.append(ip)
#     ax = timeit.timeit("qsax(L2)", globals=globals(), number=1)
#     ax_res.append(ax)

# N = np.array(list(n_range))
# ip_data = np.array(ip_res)
# ax_data = np.array(ax_res)

# # plotting
# plt.figure()
# plt.scatter(N, ip_data, s=0.5, label="in-place")
# plt.scatter(N, ax_data, s=0.5, label="auxiliary")
# plt.legend()
# plt.show()

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
