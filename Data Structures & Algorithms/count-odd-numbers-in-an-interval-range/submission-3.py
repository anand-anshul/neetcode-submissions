class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Total numbers in range is (high - low + 1)
        # If either low or high is odd, the count is (high - low) // 2 + 1
        # Otherwise, the count is (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low) // 2