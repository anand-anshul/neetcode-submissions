class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(0, 0, [], n, res)
        return res

    def backtrack(self, openP, closeP, candidate, n, res):
        if openP == closeP == n:
            res.append("".join(candidate.copy()))
            return

        if openP < n:
            candidate.append("(")
            self.backtrack(openP+1, closeP, candidate, n, res)
            candidate.pop()

        if openP > closeP:
            candidate.append(")")
            self.backtrack(openP, closeP+1, candidate, n, res)
            candidate.pop()
