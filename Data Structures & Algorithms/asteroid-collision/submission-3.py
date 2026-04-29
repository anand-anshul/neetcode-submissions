class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astro in asteroids:
            if astro < 0:
                alive = True
                while stack and alive and stack[-1] > 0:
                    if stack[-1] > abs(astro):
                        alive = False
                    elif stack[-1] == abs(astro):
                        stack.pop()
                        alive = False
                    else:
                        stack.pop()
                if alive:
                    stack.append(astro)
            else:
                stack.append(astro)

        return stack