class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visit = set()

        def dfs(i, j):
            if (
                min(i, j) < 0 or
                i >= ROWS or j >= COLS or
                (i, j) in visit or
                grid[i][j] == 0
            ):
                return 0

            visit.add((i, j))
            

            return (1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visit:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea
            