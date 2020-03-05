# 57. 面试题 - II. 和为s的连续正数序列
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1  # 滑动窗口的左边界
        j = 1  # 滑动窗口的右边界
        sum_num = 0  # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sum_num < target:
                # 右边界向右移动
                sum_num += j
                j += 1
            elif sum_num > target:
                # 左边界向右移动
                sum_num -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 右边界向右移动
                sum_num -= i
                i += 1
        print(res)


test = Solution()
test.findContinuousSequence(9)


# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         i, j = 0, 1
#         ret = []
#         mid = target // 2 + 2
#         nums = list(range(1, mid))
#         while i <= mid - 1 and j <= mid:
#             total = sum(nums[i:j])
#             if total > target:
#                 i += 1
#             elif total < target:
#                 j += 1
#             else:
#                 ret.append(nums[i:j])
#                 i += 1
#                 j += 1
#         print(ret)
#
#
# test = Solution()
# test.findContinuousSequence(9)
