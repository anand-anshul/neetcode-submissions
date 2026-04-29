class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal = float('inf')

        curSum = 0
        l = 0

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minimal = min(minimal, r - l + 1)
                curSum -= nums[l]
                l += 1
        return 0 if minimal == float('inf') else minimal
