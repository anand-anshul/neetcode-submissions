class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        dp = [[0] * (n + 1) for _ in range(m)]

        for i in range(m):
            dp[i][0] = 0
        for j in range(n + 1):
            if weight[0] <= j:
                dp[0][j] = profit[0]

        for r in range(1, m):
            for c in range(1, n + 1):
                skip = dp[r - 1][c]
                include = 0
                if weight[r] <= c:
                    include = profit[r] + dp[r - 1][c - weight[r]]
                dp[r][c] = max(skip, include)
        return dp[-1][-1]