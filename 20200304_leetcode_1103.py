# 1103. 分糖果 II
from typing import List


class Solution:
    @staticmethod
    def distributeCandies(candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies > i:
            ans[i % num_people] += i + 1
            print("第{}次：{}".format(i+1, ans))
            candies -= i + 1  # candies = candies - (i + 1)
            i += 1
            # ans[i % num_people] += candies
            # print("结果：{}".format(ans))
        ans[i % num_people] += candies
        print("结果：{}".format(ans))


test = Solution()
test.distributeCandies(10, 3)
 
