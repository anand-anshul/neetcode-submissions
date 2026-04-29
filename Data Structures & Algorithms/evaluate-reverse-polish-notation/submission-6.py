class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                first, second = stack.pop(), stack.pop()
                ans = first + second
                stack.append(ans)
            elif token == "-":
                first, second = stack.pop(), stack.pop()
                ans = second - first
                stack.append(ans)
            elif token == "*":
                first, second = stack.pop(), stack.pop()
                ans = first * second
                stack.append(ans)
            elif token == "/":
                first, second = stack.pop(), stack.pop()
                ans = int(float(second) / first)
                stack.append(ans)
            else:
                num = int(token)
                stack.append(num)
        return int(stack[-1])