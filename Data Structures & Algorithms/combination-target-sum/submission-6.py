class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(0, [], nums, target, res)
        return res

    def backtrack(self, start, candidate, nums, target, res):
        if sum(candidate) == target:
            res.append(candidate.copy())
            return

        if sum(candidate) > target:
            return

        for i in range(start, len(nums)):
            candidate.append(nums[i])
            self.backtrack(i, candidate, nums, target, res)
            candidate.pop()