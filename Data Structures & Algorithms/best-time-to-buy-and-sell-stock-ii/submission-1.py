class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_prof = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                total_prof += profit
        return total_prof