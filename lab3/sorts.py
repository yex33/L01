import random


def partition(L, low, high):
    i = low - 1
    pivot = L[high]
    for j in range(low, high):
        if L[j] <= pivot:
            i += 1
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
    L[i+1], L[high] = L[high], L[i+1]
    return i + 1


def quicksort_inplace(l, low=0, high=None):
    if high == None:
        high = len(l) - 1
    if low < high:
        p = partition(l, low, high)
        quicksort_inplace(l, low, p-1)
        quicksort_inplace(l, p+1, high)


def create_random_list(n):
    l = []
    for _ in range(n):
        l.append(random.randint(1, n))
    return l


a = create_random_list(10)

print(a)
quicksort_inplace(a)
print(a)
