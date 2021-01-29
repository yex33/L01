import timeit

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# analysis for f(n)
# reading data
fn = np.genfromtxt("fn.csv", delimiter=',', skip_header=1)
n = fn[:, 0]
f = fn[:, 1]

# linear regression using sklearn.linear_model
X = n.reshape((-1, 1))
reg = LinearRegression().fit(X, f)
a, b, rsq = *reg.coef_, reg.intercept_, reg.score(X, f)

# linear regression graph
plt.figure()
plt.scatter(n, f, s=0.3)  # f(n) plot
x = n
y = a * n + b
plt.plot(x, y, "r", lw=0.5)
plt.title("Linear regression on $f(n)$")
plt.xlabel("$n$")
plt.ylabel("Runtime")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[len(x) // 6], y[2 * len(y) // 3]))
plt.savefig("fn-linreg.png", dpi=300)

# log-log graph
n = np.log(fn[:, 0])
f = np.log(fn[:, 1])

# linear regression using sklearn.linear_model
X = n.reshape((-1, 1))
reg = LinearRegression().fit(X, f)
a, b, rsq = *reg.coef_, reg.intercept_, reg.score(X, f)

# log-log plot
plt.figure()
plt.scatter(n, f, s=0.3)  # f(n) plot
x = n
y = a * n + b
plt.plot(x, y, "r", lw=0.5)
plt.title("Log-log plot of $f(n)$ and its linear regression")
plt.xlabel("$\log{n}$")
plt.ylabel("Runtime - log")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[4], y[len(y) // 3]))
plt.savefig("fn-log-linreg.png", dpi=300)




# copy complexity test
# ns = range(100, 10000, 100)
# results = []
# for n in ns:
    # setup = "import random; L = [random.random() for _ in range(n)]"
    # stmt = "_ = L.copy()"
    # turn = min(timeit.repeat(stmt, setup, globals=globals(), repeat=5, number=100))
    # results.append(turn)
# 
# x = np.array(list(ns))
# y = np.array(results)
# plt.scatter(x, y, s=0.5)
