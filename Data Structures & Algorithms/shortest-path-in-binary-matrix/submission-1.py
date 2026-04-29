class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        length = 1
        q = deque()
        q.append((0, 0))
        visit = set()
        visit.add((0, 0))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1],
                      [1, 1], [1, -1], [-1, -1], [-1, 1]]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr >= ROWS or
                        nc >= COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1
                    ):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1

                    

                
                    
