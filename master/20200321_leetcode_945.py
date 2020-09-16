# 945. 使数组唯一的最小增量 Minimum Increment to Make Array Unique

# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
#
# Return the least number of moves to make every value in A unique.
from typing import List


class Solution:
    @staticmethod
    def minIncrementForUnique(listA: list) -> int:
        # 贪心算法
        A.sort()
        count = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                count += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        print(count)


A = [3, 2, 1, 2, 1, 7]
test = Solution()
test.minIncrementForUnique(A)
