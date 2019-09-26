# author: ptj

# 问题：设计一个双端循环队列。

class CircularDeque:
    def __init__(self, max_size: int):
        self._max_size, self._deque = max_size, []

    def insert_front(self, value: int) -> bool:
        if not self.is_full():
            self._deque.insert(0, value)
            return True
        return False

    def insert_last(self, value: int) -> bool:
        if not self.is_full():
            self._deque.append(value)
            return True
        return False

    def delete_front(self) -> bool:
        return not self.is_empty() and self._deque.pop(0) < float('inf')

    def delete_last(self) -> bool:
        return not self.is_empty() and self._deque.pop() < float('inf')

    def get_front(self) -> int:
        return self._deque[0] if self._deque else -1

    def get_rear(self) -> int:
        return self._deque[-1] if self._deque else -1

    def is_empty(self) -> bool:
        return len(self._deque) == 0

    def is_full(self) -> bool:
        return len(self._deque) >= self._max_size
