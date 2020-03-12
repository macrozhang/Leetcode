# 1071. 字符串的最大公因子


class Solution:
    @staticmethod
    def gcdOfStrings(str1: str, str2: str) -> str:
        i = j = 0
        m, n = len(str1), len(str2)
        while i < m or j < n:
            if str1[i % m] != str2[j % n]:
                return ""
            i += 1
            j += 1

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        return str1[:gcd(m, n)]


# 此题本质就是求解最大公约数:
# 从左向右遍历str1和str2
# 如果str1和str2不等，直接返回“”
# 最终返回str1和str2长度的最大公约数即可
# 复杂度分析:
# 时间复杂度：O(max(m, n))O(max(m,n))
# 空间复杂度：O(log(min(m,n)))O(log(min(m,n)))
