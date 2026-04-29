class Solution:
    def maxArea(self, high: List[int]) -> int:
        l, r = 0, len(high) - 1
        maxHigh = 0
        while l < r:
            area = (r - l) * min(high[l], high[r])
            maxHigh = max(maxHigh, area)
            if high[l] < high[r]:
                l += 1
            elif high[l] > high[r]:
                r -= 1
            else:
                r -= 1
                l += 1
        return maxHigh
            