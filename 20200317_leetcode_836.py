# 836. 矩形重叠 Longest Palindrome
from typing import List


class Solution:
    @staticmethod
    def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:

        x1 = max(rec1[0], rec2[0])
        y1 = max(rec1[1], rec2[1])

        x2 = min(rec1[2], rec2[2])
        y2 = min(rec1[3], rec2[3])

        if x1 < x2 and y1 < y2:
            return True
        else:
            return False


# 平面几何，可行域的交集

