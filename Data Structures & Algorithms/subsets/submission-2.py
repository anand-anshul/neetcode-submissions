class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, nums, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i + 1, nums, cur)
            cur.pop()
            dfs(i + 1, nums, cur)

            return res

        dfs(0, nums, [])
        return res
