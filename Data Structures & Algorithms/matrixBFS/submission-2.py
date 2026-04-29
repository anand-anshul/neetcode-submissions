class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                nein = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in nein:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visited or
                        grid[r + dr][c + dc] == 1):
                        continue
                    q.append((r + dr , c + dc))
                    visited.add((r + dr , c + dc))
            length += 1

        return -1