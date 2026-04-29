class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        lands = 0
        visit = set()

        def dfs(i, j, visit):
            if (
                min(i, j) < 0 or
                i >= ROWS or j >= COLS or
                (i, j) in visit or
                grid[i][j] == "0"
            ):
                return

            visit.add((i, j))
            dfs(i + 1, j, visit)
            dfs(i, j + 1, visit)
            dfs(i - 1, j, visit)
            dfs(i, j - 1, visit)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visit:
                    lands += 1
                    dfs(i, j, visit)

        return lands
