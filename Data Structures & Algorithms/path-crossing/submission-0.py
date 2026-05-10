class Solution:
    def isPathCrossing(self, path: str) -> bool:
        marks = set()
        cur = [0, 0]
        marks.add(tuple(cur))

        for d in path:
            if d == 'N':
                cur[1] += 1
            elif d == 'S':
                cur[1] -= 1
            elif d == 'E':
                cur[0] += 1
            elif d == 'W':
                cur[0] -= 1

            if tuple(cur) in marks:
                return True

            marks.add(tuple(cur))

        return False
            
