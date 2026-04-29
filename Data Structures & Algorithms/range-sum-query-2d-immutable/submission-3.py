class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS, COLS = len(matrix), len(matrix[0])
        self.preMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.preMatrix[r + 1][c + 1] = matrix[r][c] + self.preMatrix[r][c + 1] + self.preMatrix[r + 1][c] - self.preMatrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1


        return self.preMatrix[row2][col2] - self.preMatrix[row1 - 1][col2] - self.preMatrix[row2][col1 - 1] + self.preMatrix[row1 - 1][col1 - 1]