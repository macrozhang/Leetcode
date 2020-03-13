# 300. 最长上升子序列
# Dynamic programming.


class Solution:
    @staticmethod
    def lengthOfLIS(nums: list) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))
        return max(dp)


test = Solution()
test.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

# 动态规划
# 可参考 最长上升子序列（动态规划 + 二分查找）
