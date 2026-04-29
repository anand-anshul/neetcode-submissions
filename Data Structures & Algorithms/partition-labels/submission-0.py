class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastI = {}

        for i, c in enumerate(s):
            lastI[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastI[c] > end:
                end = lastI[c]
            if i == end:
                res.append(size)
                size = 0
        return res