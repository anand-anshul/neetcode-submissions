from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # guard for empty matrix
        if not matrix or not matrix[0]:
            self.summat = [[0]]
            return

        rows = len(matrix)
        cols = len(matrix[0])
        # (rows+1) x (cols+1) prefix matrix with 1-based indexing
        self.summat = [[0] * (cols + 1) for _ in range(rows + 1)]

        # build full 2D prefix sums
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.summat[r][c] = (
                    matrix[r-1][c-1]
                    + self.summat[r-1][c]
                    + self.summat[r][c-1]
                    - self.summat[r-1][c-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # shift to 1-based
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.summat[r2][c2]
            - self.summat[r1 - 1][c2]
            - self.summat[r2][c1 - 1]
            + self.summat[r1 - 1][c1 - 1]
        )
