class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]