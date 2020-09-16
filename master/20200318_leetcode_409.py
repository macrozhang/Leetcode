# 409. 最长回文串
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 统计字符词频
        s_cnt = collections.Counter(s)
        center = 0
        res = 0
        lis, lis1 = [], []
        listCenter = 0
        for char in s_cnt:
            # 判断各个字符的词频奇偶
            if s_cnt[char] % 2:
                center = 1  # 若出现奇数频次，center置为1
                res += s_cnt[char] - 1
                listCenter = char
            else:
                res += s_cnt[char]
                lis.append(char)
        lis1 = lis.copy()
        lis.append(listCenter)
        lis1.reverse()
        lis.extend(lis1)
        print("输出最长回文：{}, \n最长回文字符长度：{}".format(lis, res + center))
        # return res + center


test = Solution()
test.longestPalindrome("aassddffgghhjkkll")


"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        import collections
        # 1.统计各字符次数，eg:"ddsad":[3, 1, 1]
        count = collections.Counter(s).values()
        # 2.统计两两配对的字符总个数，eg: {"ddass":4,"ddsss":4}
        x = sum([item//2*2 for item in count if (item//2 > 0)])
        # 3.判断是否有没配对的单字符，有结果加一。 eg: {"ddss":4, "ddhjSS":4+1}-->{"ddss":4, "ddhjSS":5}
        return x if x == len(s) else x+1
"""


"""
组回文字符串的过程，其实我们可以看作是从一个中心往旁边对称放字符的过程。

首先我们先把给的字符串统计词频
（1）对于所有的出现偶数次的字符，那么其实在组回文字符串的时候就是可以看作直接放置在中心两侧，
因此有多少就直接加上去多少就好了。
（2）对于所有的出现奇数次的字符，那么实际上我们就可以看作是1 + 偶数次，偶数次统统可以加上去，
剩下的都是单个的不同的字符，选一个作为中心就好了。

要注意的是，如果给的字符串全是偶数次，那么肯定中心就不会一个单一的字符，
所以要加一个判断，如果出现了有字符是奇数次那么就+1，否则对于全是偶数次的字符，就不需要加1了。
"""