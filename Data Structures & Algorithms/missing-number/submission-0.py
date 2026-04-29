class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        [0, 1, 2, 3]

        [0, 1, 3]

        n = len(nums)

        for i in range(len(nums)):
            n = i - nums[i] + n

        return n
        