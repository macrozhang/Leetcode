# 204 计数质数 (本质埃氏筛法)   


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

