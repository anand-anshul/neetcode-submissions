class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m, n = len(coins), amount
        INF = amount + 1
        dp = [[INF] * (amount + 1) for _ in range(m)]

        for r in range(m):
            dp[r][0] = 0

        for c in range(1, n + 1):
            if c % coins[0] == 0:
                dp[0][c] = c // coins[0]
        
        for r in range(1, m):
            for c in range(1, n + 1):
                skip = dp[r - 1][c]
                include = INF
                if coins[r] <= c:
                    include = 1 + dp[r][c - coins[r]]
                dp[r][c] = min(skip, include)
        return -1 if dp[-1][-1] == INF else dp[-1][-1]