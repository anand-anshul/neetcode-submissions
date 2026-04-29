class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        minlr = [0] * n
        res = [0] * n

        lmax[0] = 0
        for l in range(1, n):
            lmax[l] = max(lmax[l - 1], height[l - 1])
        
        rmax[n - 1] = 0
        for r in range(n - 2, -1, -1):
            rmax[r] = max(rmax[r + 1], height[r + 1])

        for i in range(n):
            minlr[i] = min(lmax[i], rmax[i])

        for j in range(n):
            res[j] = max(0, minlr[j] - height[j])
        return sum(res)