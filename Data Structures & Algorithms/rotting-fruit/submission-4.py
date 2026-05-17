class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while q and fresh > 0:
            q_size = len(q)
            for i in range(q_size):
                r, c = q.popleft()
                for d in dirn:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1