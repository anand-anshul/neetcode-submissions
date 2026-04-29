class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                dirn = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in dirn:
                    if (
                        (r + dr) < 0 or (c + dc) < 0 or
                        (r + dr) == ROWS or (c + dc) == COLS or
                        (r + dr, c + dc) in visit or
                        grid[r + dr][c + dc] == -1
                    ):
                        continue
                    visit.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
            dist += 1



































