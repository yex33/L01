from random import randint, shuffle
from heap import Heap
from k_heap import KHeap

a = [randint(0, 100) for _ in range(63)]
print(Heap(a))
# print(heap.data)
# print(heap)
