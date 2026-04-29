class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for tok in tokens:
            if tok == "+":
                s.append(s.pop() + s.pop())
            elif tok == "-":
                snd = s.pop()
                s.append(s.pop() - snd)
            elif tok == "*":
                s.append(s.pop() * s.pop())
            elif tok == "/":
                snd = s.pop()
                s.append(int(float(s.pop()) / snd))
            else:
                s.append(int(tok))
        return s.pop()