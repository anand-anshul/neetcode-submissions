class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        
        dp = [[0] * (n + 1) for _ in range(m)]

        for r in range(m):
            dp[r][0] = 1

        for c in range(1, n + 1):
            if c % coins[0] == 0:
                dp[0][c] = 1

        for r in range(1, m):
            for c in range(1, n + 1):
                skip = dp[r - 1][c]
                include = 0
                if c >= coins[r]:
                    include = dp[r][c - coins[r]]
                dp[r][c] = skip + include

        return dp[-1][-1]