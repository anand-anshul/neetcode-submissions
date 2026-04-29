class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        k = len(s1)

        for c in s1:
            counts1[c] += 1

        l = 0
        for r in range(len(s2)):
            counts2[s2[r]] += 1
            while r - l + 1 > len(s1):
                counts2[s2[l]] -= 1
                if counts2[s2[l]] == 0:
                    del counts2[s2[l]]
                
                l += 1
            if (r - l + 1) == k and counts1 == counts2:
                return True
        return False