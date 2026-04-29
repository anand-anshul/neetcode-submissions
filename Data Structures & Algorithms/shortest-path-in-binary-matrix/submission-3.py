class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        q = deque()
        q.append((0, 0))
        visit = set((0, 0))
        dirn = [(1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (-1, -1), (1, -1), (-1, 1)]
        length = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return length
                for dr, dc in dirn:
                    nr, nc = r + dr, c + dc
                    if (
                        min(nr, nc) < 0 or
                        nr >= n or nc >= n or
                        grid[nr][nc] == 1 or
                        (nr, nc) in visit 
                    ):
                        continue
                    visit.add((nr, nc))
                    q.append((nr, nc))
            length += 1

        return -1

