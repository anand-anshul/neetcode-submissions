class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp_total = 0
        n = len(nums)
        for i in range(n + 1):
            exp_total += i

        act_total = sum(nums)

        return exp_total - act_total

        