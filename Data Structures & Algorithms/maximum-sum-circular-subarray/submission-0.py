class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glbmax, glbmin = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0

        for num in nums:
            curmax = max(curmax + num, num)
            curmin = min(curmin + num, num)
            total += num
            glbmax = max(glbmax, curmax)
            glbmin = min(glbmin, curmin)

        return max(glbmax, total - glbmin) if glbmax > 0 else glbmax