class Solution:
    def arrangeCoins(self, n: int) -> int:
        diff = n
        for i in range(1, n + 1):
            diff = diff - i
            if diff == 0:
                return i
            if diff < 0:
                return i - 1