from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))
        
        def appendcell(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or grid[r][c] != 1):
                return
            
            visit.add((r, c))
            q.append((r, c))
            fresh -= 1     # <-- correctly updates fresh
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                appendcell(r + 1, c)
                appendcell(r - 1, c)
                appendcell(r, c + 1)
                appendcell(r, c - 1)
            time += 1

        return time if fresh == 0 else -1
