class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        res = []

        def backtrack(i, cur):
            if i >= len(s):
                res.append(" ".join(cur))
                return

            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in words:
                    cur.append(w)
                    backtrack(j + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return res
