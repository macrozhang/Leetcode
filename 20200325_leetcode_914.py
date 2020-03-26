# 914. 卡牌分组
import collections


class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                # print(count.values()) [2, 4]
                if all(v % X == 0 for v in count.values()):
                    print(True)
                    return True
        print(False)
        return False


test = Solution()
test.hasGroupsSizeX([1, 1, 2, 2, 2, 2])


# all()如果iterable中的所有项目都为true，则该函数返回True，否则返回False。
#
# 如果可迭代对象为空，则该all() 函数还返回True。

