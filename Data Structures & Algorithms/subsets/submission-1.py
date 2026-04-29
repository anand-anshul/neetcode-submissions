class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curset = [], []
        def helper(i, subsets, curset, nums):
            if i >= len(nums):
                subsets.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i + 1, subsets, curset, nums)
            curset.pop()

            helper(i + 1, subsets, curset, nums)

        helper(0, subsets, curset, nums)
        return subsets