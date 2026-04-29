class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        dia_set = set()
        anti_dia_set = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if (
                    c in col_set or
                    (r + c) in dia_set or
                    (r - c) in anti_dia_set
                ):
                    continue
                col_set.add(c)
                dia_set.add(r + c)
                anti_dia_set.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col_set.remove(c)
                dia_set.remove(r + c)
                anti_dia_set.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
                
