class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.backtrack(0, [], digitToChar, digits, res)
        return res


    def backtrack(self, i, candidate, digitToChar, digits, res):
        if i == len(digits):
            res.append("".join(candidate.copy()))
            return
        for c in digitToChar[digits[i]]:
            candidate.append(c)
            self.backtrack(i+1, candidate, digitToChar, digits, res)
            candidate.pop()
        