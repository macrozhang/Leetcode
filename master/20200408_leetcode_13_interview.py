# 面试题13. 机器人的运动范围


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # 计算位数的和
        def add_coor(a, b):
            ans = 0
            while a != 0:
                ans += a % 10
                a //= 10
            while b != 0:
                ans += b % 10
                b //= 10
            return ans

        from collections import deque
        mat = [[0 for _ in range(n)] for _ in range(m)]  # 先创建 m x n 的矩阵并都设为 0
        mat[0][0] = 1   # 将初始位置设为1，代表已经访问过
        temp = deque()  # 用一个队列存储即将扩展的点的坐标
        temp.append([0, 0])
        res = 0
        # BFS经典模板
        while temp:
            temp_point = temp.popleft()
            res += 1
            x, y = temp_point
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_x = x + x_bias
                new_y = y + y_bias
                if new_x < 0 or new_x > m - 1 or new_y < 0 or new_y > n - 1 or add_coor(new_x, new_y) > k or mat[new_x][\
                         new_y] == 1:
                    continue
                mat[new_x][new_y] = 1
                temp.append([new_x, new_y])
        return res

