class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, arr, cur, cursum):
            if cursum == target:
                res.append(cur.copy())
                return
            if i >= len(arr) or cursum > target:
                return


            cur.append(arr[i])
            cursum += arr[i]
            dfs(i + 1, arr, cur, cursum)

            cur.pop()
            cursum -= arr[i]
            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                i += 1
            dfs(i + 1, arr, cur, cursum)

        dfs(0, candidates, [], 0)
        return res
             