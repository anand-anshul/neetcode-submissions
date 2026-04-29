class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(set(), [], nums, res)
        return res


    def backtrack(self, used, candidate, nums, res):
        if len(candidate) == len(nums):
            res.append(candidate.copy())
            return

        for i in range(len(nums)):
            if nums[i] not in used:
                candidate.append(nums[i])
                used.add(nums[i])
                self.backtrack(used, candidate, nums, res)
                candidate.pop()
                used.remove(nums[i])