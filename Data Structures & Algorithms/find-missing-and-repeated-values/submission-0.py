class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = defaultdict(int)

        SIDE = len(grid)

        for r in range(SIDE):
            for c in range(SIDE):
                count[grid[r][c]] += 1

        res = [0, 0]
        for i in range(1, SIDE * SIDE + 1):
            if count[i] == 0:
                res[1] = i
            if count[i] == 2:
                res[0] = i

        return res

            