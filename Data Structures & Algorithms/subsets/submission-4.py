class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
        self.backtrack(i+1, candidate, nums, res)