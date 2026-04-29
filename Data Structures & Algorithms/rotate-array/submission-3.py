class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotated = [None] * len(nums)

        for i in range(len(nums)):
            rotated[(i + k) % len(nums)] = nums[i]

        nums[:] = rotated

