class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, value in enumerate(nums):
            ans[i] = ans[n + i] = value
        return ans