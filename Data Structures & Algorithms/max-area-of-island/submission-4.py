class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (
                not (0 <= r < ROWS and 0 <= c < COLS) or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0
            
            visited.add((r, c))
            cur_area = 1

            for dr, dc in dirn:
                nr, nc = r + dr, c + dc
                cur_area += dfs(nr, nc)
            
            return cur_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area