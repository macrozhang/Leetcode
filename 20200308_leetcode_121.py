#  121. 买卖股票的最佳时机
from typing import List


class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        # inf = int(1e9)
        minprice = int(1e9)
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
            # 当然可以通过调试看得更清楚
            # print(maxprofit)
            # print(minprice)
            # print("{}循环结束".format(price))
        print()
        print(maxprofit)


test = Solution()
test.maxProfit([7, 1, 5, 3, 6, 4])

