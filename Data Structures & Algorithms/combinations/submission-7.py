class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, candidate):
            if len(candidate) == k:
                res.append(candidate.copy())
                return

            if i > n:
                return

            candidate.append(i)
            backtrack(i + 1, candidate)
            candidate.pop()
            backtrack(i + 1, candidate)
        backtrack(1, [])
        return res