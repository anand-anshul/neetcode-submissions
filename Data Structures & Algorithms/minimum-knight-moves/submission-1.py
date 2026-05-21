class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        dirn = [
            (2, 1), (2, -1), (-2, 1), (-2, -1), 
            (1, 2), (-1, 2), (1, -2), (-1, -2)
        ]
        q = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        level = 0

        while q:
            level_size = len(q)

            for i in range(level_size):
                r, c = q.popleft()
                if (r, c) == (x, y):
                    return level
                for d in dirn:
                    nr, nc = r + d[0], c + d[1]
                    if (nr, nc) not in visited and nr >= -2 and nc >= -2:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            level += 1

        return level