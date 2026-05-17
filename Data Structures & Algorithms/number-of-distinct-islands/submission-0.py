class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                (r,  c) in visited or
                grid[r][c] == 0
            ):
                return

            visited.add((r, c))
            
            current_island.add((r - o_r, c - o_c))


            for d in dirn:
                nr, nc = r + d[0], c + d[1]
                dfs(nr, nc)

        unique_islands = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_island = set()
                    o_r = r
                    o_c = c
                    dfs(r, c)
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)
                    