class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif o == "D":
                score = 2 * stack[-1]
                stack.append(score)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))

        total = 0
        for s in stack:
            total += s
        return total