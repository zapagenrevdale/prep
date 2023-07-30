from typing import List, Generic, TypeVar


T = TypeVar("T", int, str, float, bool)


class Heap(Generic[T]):
    def __init__(self) -> None:
        self.heap: List[T] = []

    def add(self, *args: T) -> None:
        for value in args:
            self.heap.append(value)
            i: int = len(self.heap) - 1
            p_i: int = (i - 1) // 2
            while p_i > -1 and self.heap[p_i] < self.heap[i]:
                self.heap[p_i], self.heap[i] = self.heap[i], self.heap[p_i]

                i = p_i
                p_i = (i - 1) // 2

    def remove(self, value: T) -> None:
        p_i: int = self.heap.index(value)
        last_val = self.heap.pop()

        if p_i < 0 or p_i == len(self.heap):
            return

        self.heap[p_i] = last_val
        while True:
            cl_i = 2 * p_i + 1
            cr_i = 2 * p_i + 2
            if cr_i < len(self.heap):
                if self.heap[cl_i] < self.heap[cr_i]:

                    cl_i = cr_i
            if cl_i >= len(self.heap) or self.heap[p_i] >= self.heap[cl_i]:
                break

            self.heap[p_i], self.heap[cl_i] = (
                self.heap[cl_i],
                self.heap[p_i],
            )