class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top, bot = 0, ROW - 1

        resRow = -1

        while top <= bot:
            M = (top + bot) // 2

            if target < matrix[M][0]:
                bot = M - 1
            elif target > matrix[M][COL - 1]:
                top = M + 1
            else:
                resRow = M
                break

        res = matrix[resRow]
        l, r = 0, COL - 1

        while l <= r:
            m = (l + r) // 2
            if target > res[m]:
                l = m + 1
            elif target < res[m]:
                r = m - 1
            else:
                return True

        return False
