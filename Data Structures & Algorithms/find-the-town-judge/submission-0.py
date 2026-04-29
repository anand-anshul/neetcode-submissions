class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        income = defaultdict(int)
        outgo = defaultdict(int)

        for src, dst in trust:
            outgo[src] += 1
            income[dst] += 1

        for i in range(1, n + 1):
            if outgo[i] == 0 and income[i] == n - 1:
                return i

        return -1