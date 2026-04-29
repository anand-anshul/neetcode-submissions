class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax, gMin = nums[0], nums[0]
        cMax, cMin = 0, 0
        total = 0

        for num in nums:
            cMax = max(cMax + num, num)
            cMin = min(cMin + num, num)
            total += num
            gMax = max(gMax, cMax)
            gMin = min(gMin, cMin)

        return max(gMax, total - gMin) if gMax > 0 else gMax