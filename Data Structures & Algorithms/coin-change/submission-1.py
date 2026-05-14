class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def top_down(coins, amount, memo):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            min_coins = float('inf')
            for coin in coins:
                if coin <= amount:
                    min_coins = min(
                        min_coins,
                        1 + top_down(coins, amount - coin, memo)
                    )
            memo[amount] = min_coins
            return memo[amount]

        min_coins = top_down(coins, amount, {})
        return min_coins if min_coins != float('inf') else -1