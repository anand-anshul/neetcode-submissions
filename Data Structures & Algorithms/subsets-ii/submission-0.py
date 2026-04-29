class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets, curset = [], []

        def helper(i, nums, subsets, curset):
            if i >= len(nums):
                subsets.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i + 1, nums, subsets, curset)
            curset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, subsets, curset)
        
        helper(0, nums, subsets, curset)
        return subsets