class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    visit.add((i, j))
        
        dirn = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minutes = 0

        while q and fresh > 0:
            for i in range(len(q)):
                
                r, c = q.popleft()

                for dr, dc in dirn:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1








