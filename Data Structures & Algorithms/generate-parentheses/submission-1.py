class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, openP, closeP):
            if openP == closeP == n:
                res.append("".join(cur.copy()))
                return

            if openP < n:
                cur.append("(")
                dfs(cur, openP + 1, closeP)
                cur.pop()
            if closeP < openP:
                cur.append(")")
                dfs(cur, openP, closeP + 1)
                cur.pop()

        dfs([], 0, 0)
        return res