class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        cur_min, cur_max = 1, 1

        for num in nums:
            tmp = num * cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, tmp, num * cur_min)
            res = max(res, cur_max)

        return res