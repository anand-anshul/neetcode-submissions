class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(0, [], candidates, target, res)
        return res



    def backtrack(self, i, subset, candidates, target, res):

        if sum(subset) == target:
            res.append(subset.copy())
            return
        if sum(subset) > target or i == len(candidates):
            return

        subset.append(candidates[i])
        self.backtrack(i+1, subset, candidates, target, res)

        subset.pop()
        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        self.backtrack(i+1, subset, candidates, target, res)