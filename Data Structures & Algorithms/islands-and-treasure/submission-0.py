class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])

        def appendroom(r, c):
            if (min(r, c) < 0 or
                r == rows or c == cols or
                (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                appendroom(r + 1, c)
                appendroom(r, c + 1)
                appendroom(r - 1, c)
                appendroom(r, c - 1)
            dist += 1









