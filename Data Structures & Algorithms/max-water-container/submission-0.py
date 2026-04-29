class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxarea = 0

        while L < R:
            area = min(height[L], height[R]) * (R - L)
            maxarea = max(maxarea, area)
            if height[L] < height[R]:
                L += 1
            elif height[L] > height[R]:
                R -= 1
            else:
                L += 1
                R -= 1
        return maxarea

