# 面试题 01.07. 旋转矩阵
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        # 先在纵向上进行上下翻转
        # 切片会创建新的对象进而开辟新地址
        matrix[:] = matrix[::-1]
        # 然后沿对角线翻转
        for i in range(length):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
