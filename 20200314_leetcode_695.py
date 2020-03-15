#695. 岛屿的最大面积


class Solution:
    @staticmethod
    def maxAreaOfIsland(grid: list) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        ans = 0

        def dfs(row, column):
            if row < 0 or row >= m or column < 0 or column >= n:
                return 0
            if grid[row][column] == 0:
                return 0
            grid[row][column] = 0
            top = dfs(row + 1, column)
            bottom = dfs(row - 1, column)
            left = dfs(row, column - 1)
            right = dfs(row, column + 1)
            return 1 + sum([top, bottom, left, right])
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans
