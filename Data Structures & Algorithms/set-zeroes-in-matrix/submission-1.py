class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        matCop = [row[:] for row in matrix]
        
        def doZ(r, c):
            for i in range(ROWS):
                matCop[i][c] = 0

            for i in range(COLS):
                matCop[r][i] = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    doZ(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = matCop[r][c]

        