class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, k):
            if len(cur) == k:
                res.append(cur.copy())
                return

            if i > n:
                return

            cur.append(i)
            dfs(i + 1, cur, k)
            cur.pop()
            dfs(i + 1, cur, k)

            return res

        dfs(1, [], k)
        return res 