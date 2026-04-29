class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        dirn = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (n - 1, n - 1):
                return t

            for dr, dc in dirn:
                nr, nc = r + dr, c + dc
                if (
                    min(nr, nc) < 0 or
                    nr == n or nc == n or
                    (nr, nc) in visit
                ):
                    continue
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
        


