class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        m = len(nums)

        dp = [[False] * (target + 1) for _ in range(m)]

        # Base case: sum 0 is always possible
        for r in range(m):
            dp[r][0] = True

        # First row initialization
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for r in range(1, m):
            for c in range(1, target + 1):
                skip = dp[r - 1][c]
                include = False
                if c - nums[r] >= 0:
                    include = dp[r - 1][c - nums[r]]

                dp[r][c] = skip or include

        return dp[m - 1][target]
