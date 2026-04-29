class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L, R = 0, len(nums) - 1

        while L < R:
            total = nums[L] + nums[R]
            if total < target:
                L += 1
            elif total > target:
                R -= 1
            else:
                return [L + 1, R + 1]