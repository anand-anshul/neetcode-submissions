class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        level = 0
        
        while q:
            level_size = len(q)
            level += 1
            for i in range(level_size):
                r, c = q.popleft()
                for d in dirn:
                    nr, nc = r + d[0], c + d[1]
                    if (
                        min(nr, nc) >= 0 and
                        nr < ROWS and nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 2147483647
                    ):
                        grid[nr][nc] = level
                        visited.add((nr, nc))
                        q.append((nr, nc))

        

