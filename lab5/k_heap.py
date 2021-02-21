import math
from typing import Any, List


class KHeap:
    def __init__(self, values: List[Any], k: int) -> None:
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap()

    def build_heap(self) -> None:
        for i in range((self.length + 1 - self.k) // self.k, -1, -1):
            self.sink(i)

    def parent(self, i: int) -> int:
        return i // self.k

    def children(self, i: int) -> List[int]:
        start = i * self.k + 1
        return list(range(start, min(start + self.k, self.length)))

    def sink(self, i: int) -> None:
        # i is smaller than the first non-leaf index
        while i <= (self.length + 1 - self.k) // self.k:
            j = i  # index before sinking the ith element
            i = max(self.children(i) + [i], key=lambda x:self.data[x])
            if (j != i):
                self.data[i], self.data[j] = self.data[j], self.data[i]
            else:
                break

    def __str__(self):
        height = math.ceil(math.log((self.k - 1) * self.length, self.k))
        whitespace = self.k ** height
        s = ""
        for i in range(height):
            start = math.floor(self.k ** i / (self.k - 1))
            end = min(self.k ** (i + 1) // (self.k - 1), self.length)
            print(i, start, end)
            for j in range(start, end):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // self.k
        return s
