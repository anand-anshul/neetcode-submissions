class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxprof = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            else:
                maxprof = max(maxprof, profit)

        return maxprof