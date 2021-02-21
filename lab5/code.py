from random import randint, shuffle

from k_heap import KHeap

a = [randint(0, 100) for _ in range(30)]
print(a)

heap = KHeap(a, 3)
print(heap.data)
print(heap)
