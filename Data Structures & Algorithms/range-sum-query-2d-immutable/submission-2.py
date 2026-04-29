class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])

        self.matrix = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(ROW):
            for c in range(COL):
                self.matrix[r + 1][c + 1] = (
                    matrix[r][c] +
                    self.matrix[r][c + 1] +
                    self.matrix[r + 1][c] -
                    self.matrix[r][c]
                )



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1
        return (
            self.matrix[row2][col2] +
            self.matrix[row1 - 1][col1 - 1] -
            self.matrix[row1 - 1][col2] - 
            self.matrix[row2][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)