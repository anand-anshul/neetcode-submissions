class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clo2op = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if stack and c in clo2op and stack[-1] == clo2op[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack