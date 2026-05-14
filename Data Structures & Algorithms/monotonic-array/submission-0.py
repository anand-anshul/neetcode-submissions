class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        expect = 0

        if nums[0] <= nums[n-1]:
            expect = 1
        else:
            expect = -1
        
        for i in range(1, n):
            if expect == 1:
                if nums[i] < nums[i - 1]:
                    return False
            else:
                if nums[i] > nums[i - 1]:
                    return False
        return True