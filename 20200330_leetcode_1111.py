# 1111. 有效括号的嵌套深度
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans


test = Solution()
print(test.maxDepthAfterSplit("()(())()"))

"""
只要在遍历过程中，我们保证栈内一半的括号属于序列 A，一半的括号属于序列 B，
那么就能保证拆分后最大的嵌套深度最小，是当前最大嵌套深度的一半。
要实现这样的对半分配，我们只需要把奇数层的 ( 分配给 A，偶数层的 ( 分配给 B 即可。
要实现这样的对半分配，我们只需要把奇数层的 ( 分配给 A，偶数层的 ( 分配给 B 即可。
对于上面的例子，我们将嵌套深度为 1 和 3 的所有括号 (()) 分配给 A，
嵌套深度为 2 的所有括号 ()()() 分配给 B。
"""

"""
代码思路：只需要判断当前字符与前一个字符的关系
两个单括号组成的情况有四种:'((', '))', '()', ')('
前两种情况，这两个单括号肯定不能在同一子序列中，因为那样会加深字符串深度，所以分别分到A，B组
后两种情况，分到同一组不会加深字符串深度，所以可以分到同一组
"""

"""
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = [0]*len(seq)
        for i in range(1, len(seq)):
            if seq[i] == seq[i-1]: # 前后分到不同组
                res[i] = 1 - res[i-1]
            else:
                res[i] = res[i-1] # 前后同组
        return res
"""
