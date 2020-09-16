# 面试题 17.16. 按摩师 The Masseuse LCCI


class Solution(object):
    @staticmethod
    def massage(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            # 选择该预约 等于i-2的最长时长+本次预约时长
            A = dp[i - 2] + nums[i]
            # 不选择该预约，等于i-1的最长时长
            B = dp[i - 1]
            # 选择两种情况下的最长时长
            dp[i] = max(A, B)
        print(dp[-1])
        return dp[-1]


test = Solution()
test.massage([1, 2, 3, 1])



"""
解题思路：
利用常规的动态规划
1.判断nums的长度 0就返回0 1就返回第一个元素（因为我么得选择）
2.创建一个列表dp=[0] * len(nums)
3.dp的第一个元素等于nums的第一个元素，
    第二个元素等于nums的第一个元素与第二个元素的最大值
4.从索引2开始循环nums
5.两种选择。 
    1.选择该预约 则dp[i] = dp[i-2] + nums[i] 
        (若选择该预约等于i-2的最长时长+本次预约时长)
    2.不选择该预约 则dp[i] = dp[i-1] 
        (不选择该预约则最长时长仍等于上一个预约的时长)
6.返回dp最后一个元素（dp每个元素表示到该预约的最长时长）
"""