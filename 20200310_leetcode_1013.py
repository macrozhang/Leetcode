# 1013. 将数组分成和相等的三个部分


class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        sumt = sum(A)/3
        cursum = 0
        pn = 0
        for i in A:
            cursum += i
            if cursum == sumt:
                cursum = 0
                pn += 1
                if pn == 2:
                    return True
        return False

# 我们要将数组平均分成三分，那么每一份的和一定是sum(A)/3。因此我们的思路就是：
#
# 从左往右遍历，遍历的同时累加，当加到 sum(A)/3，我们cnt + 1。累加器归零
# 最后我们只要检查 cnt 大于等于 3， 且累加器归零就好了。
# 大于是为了处理和为 0 的情况.
# 时间复杂度：O(N)O(N)
# 空间复杂度：O(1)O(1)

