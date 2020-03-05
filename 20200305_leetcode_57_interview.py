# 57. 面试题 - II. 和为s的连续正数序列
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j = 0, 1
        ret = []
        mid = target // 2 + 2
        nums = list(range(1, mid))
        while i <= mid - 1 and j <= mid:
            total = sum(nums[i:j])
            if total > target:
                i += 1
            elif total < target:
                j += 1
            else:
                ret.append(nums[i:j])
                i += 1
                j += 1
        print(ret)


test = Solution()
test.findContinuousSequence(9)
