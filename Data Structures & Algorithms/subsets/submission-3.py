class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, arr, cur):
            if i >= len(arr):
                res.append(cur.copy())
                return
            cur.append(arr[i])
            dfs(i + 1, arr, cur)

            cur.pop()
            dfs(i + 1, arr, cur)

        dfs(0, nums, [])
        return res