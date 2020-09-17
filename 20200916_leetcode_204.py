# 204 计数质数 (本质埃氏筛法)  简单
# 效率提升的关键在于埃拉托斯特尼筛法，简称埃式筛，也叫厄拉多塞筛法：
# 要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。


class Solution:
    @staticmethod
    def countPrimes(n: int) -> int:
        primes = []
        st = [False] * (n + 1)
        for i in range(2, n):
            if not st[i]:
                primes.append(i)
            for prime in primes:
                if prime > n // i:
                    break
                st[prime * i] = True
                if i % prime == 0:
                    break
        return len(primes)

