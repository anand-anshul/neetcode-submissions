class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n

        for i in range(1, n):
            leftmax[i] = max(height[i - 1], leftmax[i - 1])

        for j in range(n - 2, -1, -1):
            rightmax[j] = max(height[j + 1], rightmax[j + 1])

        res = 0
        for k in range(n):
            res += max(0, min(leftmax[k], rightmax[k]) - height[k])
        return res