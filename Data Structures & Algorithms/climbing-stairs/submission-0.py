class Solution:
    def climbStairs(self, n: int) -> int:
        secLast, last = 1, 1

        for i in range(n - 1):
            temp = secLast
            secLast = secLast + last
            last = temp
        
        return secLast