import numpy as np

a = np.random.rand(5)
print(a)
print(a[-1])
print(a[-2])
print(a[-5])

# seq[start:end:step]
# [m:n] #切片操作，取a[m]~a[n-1]之间的内容，m\n可以为负，m>n时返回空
# [m::n] #从a[m]开始，每跳|n|个取一个，当n为负时逆序取数，当n为正的时候，m为空则默认m=0，n为负时，m为空则默认为-1
# 控制台直接输入以下练习:
a[3:-1]
a[2:-1]
a[3::-1]
a[2::-2]
a[:]

