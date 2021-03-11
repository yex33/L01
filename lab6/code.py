import math
import random
import sys
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

from rbt import RBTree

sys.setrecursionlimit(15000)
rc("font", **{"family": "serif", "size": 12})
rc("text", usetex=True)

# ******************** given codes ********************
def create_random_list(n):
    return [random.randint(1, 2 * n) for _ in range(n)]

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def __str__(self):
        return "(" + str(self.value) + ")"

    def __repr__(self):
         return "(" + str(self.value) + ")"


class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = BSTNode(value)
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = BSTNode(value)
                node.right.parent = node
            else:
                self.__insert(node.right, value)

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
# ******************** given codes ********************


def multi_ascend():
    rbt = RBTree()
    for k in range(4):
        for i in range(1, 10 ** 4 + 1):
            rbt.insert(i)
        print(rbt.get_height())

def run_mult(func, n, n_proc):
    with Pool(processes=n_proc) as pool:
        return pool.map(func, n)

def ins_vals(tree, L):
    for e in L:
        tree.insert(e)

def rand_comp(n):
    bst = BST()
    rbt = RBTree()
    L = create_random_list(n)
    ins_vals(bst, L.copy())
    ins_vals(rbt, L.copy())
    bsth = bst.get_height()
    rbth = rbt.get_height()
    return [bsth, rbth]

def rand_heights():
    k = 1000
    n = (10 ** 4 for _ in range(k))
    res = run_mult(rand_comp, n, 16)

    N = np.arange(1, k + 1)
    res = np.array(res)
    bsths = res[:, 0]
    rbths = res[:, 1]

    plt.figure()
    plt.scatter(N, bsths, s=1, label="BST")
    plt.scatter(N, rbths, s=1, label="RBT")
    plt.legend()
    plt.title("Heights of BST and RBT on 10,000 random numbers")
    plt.xlabel("$n$, the $n$-th set of random numbers of size 10,000")
    plt.ylabel("Height (levels)")
    plt.savefig("images/rand.png", dpi=300)

    avg_diff = np.average(np.abs(bsths - rbths))
    print(f"BST is on average {avg_diff} levels taller than RBT.")

def near_comp(args):
    k = 5  # take the average of k tests
    bsths = []
    rbths = []
    for _ in range(k):
        bst = BST()
        rbt = RBTree()
        L = create_near_sorted_list(*args)
        ins_vals(bst, L.copy())
        ins_vals(rbt, L.copy())
        bsths.append(bst.get_height())
        rbths.append(rbt.get_height())
    return [sum(bsths) / len(bsths), sum(rbths) / len(rbths)]

def near_heights():
    k = 100
    facts = np.concatenate((np.linspace(0, 1 / 4, k), np.linspace(1 / 4, 1, k)))
    n = np.array(list(10 ** 4 for _ in range(len(facts))))
    res = run_mult(near_comp, zip(n, facts), 16)

    res = np.array(res)
    bsths = res[:, 0]
    rbths = res[:, 1]

    plt.figure()
    plt.scatter(facts * 100, bsths, s=1, label="BST")
    plt.scatter(facts * 100, rbths, s=1, label="RBT")
    plt.legend()
    plt.title("Average heights of BST and RBT on 10,000 near-sorted numbers")
    plt.xlabel("Inversion Factor (\%)")
    plt.ylabel("Height (levels)")
    plt.savefig("images/near.png", dpi=300)


if __name__ == "__main__":
    multi_ascend()
    rand_heights()
    near_heights()
