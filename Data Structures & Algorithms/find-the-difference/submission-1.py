class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(s)

        for c in t:
            if counts[c] == 0:
                return c
            counts[c] -= 1