class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)

        for i in range(n):
            res += mat[i][i]
            res += mat[i][n - 1 - i]

        if n % 2 == 0:
            return res
        else:
            return res - mat[n // 2][n // 2]