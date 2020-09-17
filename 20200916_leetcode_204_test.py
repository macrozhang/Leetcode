# isPrime = [1] * 10
# isPrime[0] = isPrime[1] = 0
# print(isPrime)


def count_primes_py(n):
    """
    求n以内的所有质数个数
    """
    # 最小的质数是 2
    if n < 2:
        return 0

    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

    # 埃式筛，把不大于根号n的所有质数的倍数剔除
    # **乘方
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
            # //地板除:除法不管操作数为何种数值类型，总是会舍去小数部分，返回数字序列中比真正的商小的最接近的数字
            # 注意闭区间
    print("isPrime:", isPrime)
    # print(list(enumerate(isPrime)))
    for i, x in enumerate(isPrime):
        if x:
            print(i)
    print("The sum of prime number is:", sum(isPrime))


count_primes_py(10)
