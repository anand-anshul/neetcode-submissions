class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, curSum, nums):
            if curSum == target:
                res.append(cur.copy())
                return

            if curSum > target or i >= len(nums):
                return

            cur.append(nums[i])
            dfs(i + 1, cur, curSum + nums[i], nums)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur, curSum, nums)

        dfs(0, [], 0, nums)
        return res
