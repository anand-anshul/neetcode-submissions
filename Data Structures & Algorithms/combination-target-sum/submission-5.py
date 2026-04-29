class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, arr, cur, curSum):
            if i >= len(arr) or curSum > target:
                return
            
            if curSum == target:
                res.append(cur.copy())
                return

            cur.append(arr[i])
            curSum += arr[i]
            dfs(i, arr, cur, curSum)

            cur.pop()
            curSum -= arr[i]
            dfs(i + 1, arr, cur, curSum)

        dfs(0, nums, [], 0)
        return res