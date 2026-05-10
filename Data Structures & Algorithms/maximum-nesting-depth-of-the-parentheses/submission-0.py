class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0

        for c in s:
            if c == "(":
                stack.append(c)
                depth = max(len(stack), depth)
            elif c == ")":
                stack.pop()

        return depth