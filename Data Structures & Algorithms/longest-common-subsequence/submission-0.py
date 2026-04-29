class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                if text1[r] == text2[c]:
                    dp[r + 1][c + 1] = 1 + dp[r][c]
                else:
                    dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])

        return dp[-1][-1] 