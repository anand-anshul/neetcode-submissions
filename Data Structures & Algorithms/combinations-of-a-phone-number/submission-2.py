class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(i, cur):
            if len(cur) == len(digits):
                res.append("".join(cur.copy()))
                return
            if i > len(digits):
                return
            for c in digitToChar[digits[i]]:
                cur.append(c)
                helper(i + 1, cur)
                cur.pop()

        if digits:
            helper(0, [])
        return res