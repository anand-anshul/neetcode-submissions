class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast < 0:
                alive = True
                while stack and alive and stack[-1] > 0:
                    if stack[-1] > abs(ast):
                        alive = False
                    elif stack[-1] == abs(ast):
                        stack.pop()
                        alive = False
                    else:
                        stack.pop()
                if alive:
                    stack.append(ast)
            else:
                stack.append(ast)

        return stack
                
