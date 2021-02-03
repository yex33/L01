import timeit

import matplotlib.pyplot as plt
import numpy as np

from lab3 import create_random_list, my_quicksort
from sorts import quicksort_inplace

# in-place version timing experiments
n_range = range(1000, 100_000, 1000)
ip_res = []  # in-place version results
ax_res = []  # auxiliary array version results
for n in n_range:
    L = create_random_list(n)
    L2 = L.copy()
    qsip = quicksort_inplace
    qsax = my_quicksort
    ip = timeit.timeit("qsip(L)", globals=globals(), number=1)
    ip_res.append(ip)
    ax = timeit.timeit("qsax(L2)", globals=globals(), number=1)
    ax_res.append(ax)

N = np.array(list(n_range))
ip_data = np.array(ip_res)
ax_data = np.array(ax_res)

# plotting
plt.figure()
plt.scatter(N, ip_data, s=0.5, label="in-place")
plt.scatter(N, ax_data, s=0.5, label="auxiliary")
plt.legend()
plt.show()
