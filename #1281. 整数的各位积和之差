# 1281. 整数的各位积和之差
class Solution:
    @staticmethod
    def difference(n: int):
        add, mul = 0, 1
        while n > 0:
            digit = n % 10
            n //= 10
            add += digit
            mul *= digit
        print(mul - add)


test = Solution()
test.difference(23)
