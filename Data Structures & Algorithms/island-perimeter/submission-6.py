class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visit):
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                return 1

            if (r, c) in visit:
                return 0

            visit.add((r, c))

            res = 0
            for d in dirn:
                next_r, next_c = r + d[0], c + d[1]
                res += dfs(next_r, next_c, visit)
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c, set())

        return 0

            