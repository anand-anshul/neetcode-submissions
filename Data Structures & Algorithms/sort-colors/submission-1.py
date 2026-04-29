class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3

        for num in nums:
            bucket[num] += 1

        j = 0
        for i in range(3):
            while bucket[i] > 0:
                nums[j] = i
                bucket[i] -= 1
                j += 1
        