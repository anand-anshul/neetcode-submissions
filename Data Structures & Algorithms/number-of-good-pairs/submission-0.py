class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0

        for n, c in counts.items():
            combs = (c * (c - 1)) // 2
            res += combs

        return res
