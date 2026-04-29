class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3

        for num in nums:
            buckets[num] += 1
        
        index = 0
        for i in range(3):
            while buckets[i] > 0:
                buckets[i] -= 1
                nums[index] = i
                index += 1
            


