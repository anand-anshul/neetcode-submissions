class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDia = set()
        negDia = set()

        self.res = 0

        def backtrack(r):
            if r == n:
                self.res += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDia or (r - c) in negDia:
                    continue
                
                col.add(c)
                posDia.add(r + c)
                negDia.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posDia.remove(r + c)
                negDia.remove(r - c)

        backtrack(0)
        return self.res
