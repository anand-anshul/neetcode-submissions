class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        ROW = len(board)
        COL = len(board[0])

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                elif board[r][c] in cols[c]:
                    return False
                elif board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True 
