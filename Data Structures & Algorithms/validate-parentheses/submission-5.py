class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        bracket_stack = []

        for c in s:
            if c in close_open: 
                if bracket_stack and bracket_stack[-1] == close_open[c]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(c)
        
        return len(bracket_stack) == 0
            
