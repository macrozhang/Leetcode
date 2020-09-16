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

# 样例1，输入[[1,2],[3,4]]，34
# 这里的1意思是第一行第一列有一个立方体，2意思是第一行第二列有2个立方体，
# 3的意思是第二行第一列有3个立方体，4意思是第二行第二列有4个立方体。
# 样例2，输入：[[1,1,1],[1,0,1],[1,1,1]] 输出：32
# 三行三列方格


# 派n个小人，横向走一遍，纵向走一遍，小人上下台阶都费力，把费力值求和，加上数组中>0的个数*2就是答案
# 每个小人从平地开始，到平地。
# 在走台阶的时候，只需要记录上一次的台阶和本次台阶的差值绝对值，就是费力值。
# 横向走一遍，纵向走一遍，即只需要再次调用函数，传入numpy的转置即可
