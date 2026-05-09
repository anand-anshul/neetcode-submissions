class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            cur = nums[i]
            if (
                (cur % 2 == 0 and prev % 2 == 0) or
                (cur % 2 == 1 and prev % 2 == 1)
            ):
                return False

        return True