# 892. 三维形体的表面积
import numpy


class Solution:
    def surfaceArea(self, grid: list) -> int:

        N = len(grid)

        def S(L):
            Sum = 0
            for i in L:
                Last = 0
                for j in i:
                    Sum += abs(j-Last)
                    Last = j
                Sum += Last
            return Sum
        print(S(numpy.array(grid).T)+S(grid)+numpy.sign(grid).sum()*2)
        return S(numpy.array(grid).T)+S(grid)+numpy.sign(grid).sum()*2


test = Solution()
test.surfaceArea([[1, 2], [3, 4]])

# 亦可通过在Edit Configuration中改变Execution中的Run with Python Console测试