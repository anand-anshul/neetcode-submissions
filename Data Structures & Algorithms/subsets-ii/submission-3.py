class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.backtrack(0, [], nums, res)
        return res


    def backtrack(self, i, candidate, nums, res):
        if i == len(nums):
            res.append(candidate.copy())
            return

        candidate.append(nums[i])
        self.backtrack(i+1, candidate, nums, res)

        candidate.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.backtrack(i+1, candidate, nums, res)