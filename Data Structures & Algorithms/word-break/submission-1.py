class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtrack(i, s, wordDict, memo):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i+len(word)] == word:
                    if backtrack(i + len(word), s, wordDict, memo):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return backtrack(0, s, wordDict, {})