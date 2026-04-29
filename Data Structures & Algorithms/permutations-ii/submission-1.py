class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permuteUnique(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                if i > 0  and nums[0] == p[i - 1]:
                    break
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                res.append(pcopy)
        return res
