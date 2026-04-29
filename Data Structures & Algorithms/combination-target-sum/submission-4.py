class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, curSum, nums):
            if curSum == target:
                res.append(cur.copy())
                return
            if curSum > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i, cur, curSum + nums[i], nums)
            cur.pop()
            dfs(i + 1, cur, curSum, nums)

            return res

        dfs(0, [], 0, nums)
        return res
