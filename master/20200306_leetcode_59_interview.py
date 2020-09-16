# 面试题59 - II. 队列的最大值
import queue


class MaxQueue:
    def __init__(self):
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1


# 暴力求解法
# 时间复杂度：O(1)O(1)（插入，删除），O(n)O(n)（求最大值）。
# 插入与删除只需要普通的队列操作，为 O(1)O(1)，求最大值需要遍历当前的整个队列，最坏情况下为 O(n)O(n)。
# 空间复杂度：O(n)O(n)，需要用队列存储所有插入的元素。
