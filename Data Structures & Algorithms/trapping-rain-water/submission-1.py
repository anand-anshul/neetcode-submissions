class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        L, R = 0, len(height) - 1
        lmax, rmax = height[L], height[R]
        res = 0
        while L < R:

            if height[L] <= height[R]:
                L += 1
                lmax = max(lmax, height[L])
                res += lmax - height[L]
            
            else:
                R -= 1
                rmax = max(rmax, height[R])
                res += rmax - height[R]

        return res

