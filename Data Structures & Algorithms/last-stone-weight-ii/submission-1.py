class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStone = sum(stones)
        target = (sumStone + 1) // 2
        memo = {}

        def dfs(i, total):
            if i >= len(stones) or total > target:
                return abs(total - (sumStone - total))
            if (i, total) in memo:
                return memo[(i, total)]
            memo[(i, total)] = min(dfs(i + 1, total + stones[i]), dfs(i + 1, total)) 
            return memo[(i, total)]

        return dfs(0, 0)