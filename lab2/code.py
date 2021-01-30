import random
import timeit

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

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
plt.ylabel("Runtime (s)")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[len(x) // 6], y[2 * len(y) // 3]))
plt.savefig("images/fn-linreg", dpi=300)

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
plt.savefig("images/fn-log-linreg", dpi=300)


# analysis for g(n)
gn = np.genfromtxt("gn.csv", delimiter=',', skip_header=1)
n = gn[:, 0]
f = gn[:, 1]

# polynomial regression
X = n.reshape((-1, 1))
model = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
model.fit(X, f)
reg = model.named_steps.linearregression
coef = reg.coef_[:0:-1]
a, b, c, d, rsq = *coef, reg.intercept_, model.score(X, f)

# polynomial regression graph
plt.figure()
plt.scatter(n, f, s=0.3)  # g(n) plot
x = n
y = a * n ** 3 + b * n ** 2 + c * n + d
plt.plot(x, y, "r", lw=0.5)
plt.title("Polynomial regression on $g(n)$")
plt.xlabel("$n$")
plt.ylabel("Runtime (s)")
equation_text = (f"$y = {a:.4g}x^3 + {b:.4g}x^2 + {c:.4g}x + {d:.4g}$\n"
                 + f"$R^2 = {rsq:.4g}$")
plt.annotate(equation_text, xy=(x[1], y[-2]))
plt.savefig("images/gn-polyreg", dpi=300)

# log-log graph
n = np.log(gn[:, 0])
f = np.log(gn[:, 1])

# linear regression using sklearn.linear_model
X = n.reshape((-1, 1))
reg = LinearRegression().fit(X, f)
a, b, rsq = *reg.coef_, reg.intercept_, reg.score(X, f)

# log-log plot
plt.figure()
plt.scatter(n, f, s=0.3)  # g(n) plot
x = n
y = a * n + b
plt.plot(x, y, "r", lw=0.5)
plt.title("Log-log plot of $g(n)$ and its linear regression")
plt.xlabel("$\log{n}$")
plt.ylabel("Runtime - log")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[4], y[len(y) // 3]))
plt.savefig("images/gn-log-linreg", dpi=300)


# analysis for h(n)

hn = np.genfromtxt("hn.csv", delimiter=',', skip_header=1)
n = hn[:, 0]
f = hn[:, 1]

# Polynomial regression
X = n.reshape((-1, 1))
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X, f)
reg = model.named_steps.linearregression
coef = reg.coef_[:0:-1]
a, b, c, rsq = *coef, reg.intercept_, model.score(X, f)

# linear regression graph
plt.figure()
plt.scatter(n, f, s=0.3)  # h(n) plot
x = n
y = a * n ** 2 + b * n + c
plt.plot(x, y, "r", lw=0.5)
plt.title("Polynomial regression on $h(n)$")
plt.xlabel("$n$")
plt.ylabel("Runtime (s)")
equation_text = f"$y = {a:.4g}x^2 + {b:.4g}x + {c:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[len(x) // 2], y[-20]))
plt.savefig("images/hn-polyreg", dpi=300)

# log-log graph
n = np.log(hn[:, 0])
f = np.log(hn[:, 1])

# linear regression using sklearn.linear_model
X = n.reshape((-1, 1))
reg = LinearRegression().fit(X, f)
a, b, rsq = *reg.coef_, reg.intercept_, reg.score(X, f)

# log-log plot
plt.figure()
plt.scatter(n, f, s=0.3)  # h(n) plot
x = n
y = a * n + b
plt.plot(x, y, "r", lw=0.5)
plt.title("Log-log plot of $h(n)$ and its linear regression")
plt.xlabel("$\log{n}$")
plt.ylabel("Runtime - log")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[4], y[len(y) // 3]))
plt.savefig("images/hn-log-linreg", dpi=300)

# logarithmic regression
n = hn[:, 0]
f = hn[:, 1] / n

# logarithmic regression
a, b = np.polyfit(np.log(n), f, 1)
x = n
y = a * np.log(n) + b
rsq = np.corrcoef(f, y)[0, 1] ** 2

# logarithmic regression graph
plt.figure()
plt.scatter(n, f, s=0.3)  # h(n) plot
plt.plot(x, y, "r", lw=0.5)
plt.title("Logistic regression on $h(n) / n$")
plt.xlabel("$n$")
plt.ylabel("Runtime $/ n$")
equation_text = (f"$y = {a:.4g}$ "
                 + "$\ln{x}$"
                 + f"$+ {b:.4g}$\n$R^2 = {rsq:.4g}$")
plt.annotate(equation_text, xy=(100000, y[100]))
plt.savefig("images/hn-over-n-logreg", dpi=300)


# copy complexity test
ns = range(100, 10000, 100)
results = []
for n in ns:
    setup = "import random; L = [random.random() for _ in range(n)]"
    stmt = "_ = L.copy()"
    turn = min(timeit.repeat(stmt, setup, globals=globals(), repeat=5, number=100))
    results.append(turn)

n = np.array(list(ns))
f = np.array(results)

# linear regression
a, b = np.polyfit(n, f, 1)
x = n
y = a * x + b
rsq = np.corrcoef(f, y)[0, 1] ** 2

# graph
plt.figure()
plt.scatter(n, f, s=0.3)
plt.plot(x, y, "r", lw=0.5)
plt.title("list.copy growth and its linear regression")
plt.xlabel("$n$, length of copied list")
plt.ylabel("Runtime (s)")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[4], y[2 * len(y) // 3]))
plt.savefig("images/copy-linreg.png", dpi=300, bbox_inches="tight")

# log-log plot
n = np.log(np.array(list(ns)))
f = np.log(np.array(results))

# linear regression
a, b = np.polyfit(n, f, 1)
x = n
y = a * x + b
rsq = np.corrcoef(f, y)[0, 1] ** 2

# graph
plt.figure()
plt.scatter(n, f, s=0.3)
plt.plot(x, y, "r", lw=0.5)
plt.title("Log-log plot of the growth of list.copy")
plt.xlabel("$\ln{n}$, length of copied list - log")
plt.ylabel("Runtime - log")
equation_text = f"$y = {a:.4g}x + {b:.4g}$\n$R^2 = {rsq:.4g}$"
plt.annotate(equation_text, xy=(x[4], y[2 * len(y) // 3]))
plt.savefig("images/copy-log-linreg.png", dpi=300)


# lookup time test
n = 1_000_000
results = [0] * n
L = [random.random() for _ in range(n)]
for i in range(n):
    stmt = "_ = L[i]"
    results[i] = timeit.timeit(stmt, globals=globals(), number=10)

x = np.array(list(range(n)))
y = np.array(results)
plt.figure()
plt.scatter(x, y, s=1)
plt.title("Access each index in a list with length of 1 million")
plt.xlabel("x, lookup the x'th value")
plt.ylabel("Runtime (s)")
plt.savefig("images/lookup.png")


# append time test
n = 1_000_000
results = [0] * n
L = []
for i in range(n):
    stmt = "L.append(i)"
    results[i] = timeit.timeit(stmt, globals=globals(), number=1)

x = np.array(list(range(n)))
y = np.array(results)
plt.figure()
plt.scatter(x, y, s=1)
plt.title("Append numbers until a list reaches length of 1 million")
plt.xlabel("x, appending the x'th value")
plt.ylabel("Runtime (s)")
plt.savefig("images/append.png")

n = 1_000_000
results = [0] * n
L = []
for i in range(n):
    stmt = "L.append('append')"
    results[i] = timeit.timeit(stmt, globals=globals(), number=1)

x = np.array(list(range(n)))
y = np.array(results)
plt.figure()
plt.scatter(x, y, s=1)
plt.title("Append strings until a list reaches length of 1 million")
plt.xlabel("x, appending the x'th string")
plt.ylabel("Runtime (s)")
plt.savefig("images/append-string.png")
