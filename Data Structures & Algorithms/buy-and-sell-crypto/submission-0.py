class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProf = 0
        for r in range(1, len(prices)):
            prof = prices[r] - prices[l]
            if prof < 0:
                l = r
            maxProf = max(maxProf, prof)
        return maxProf