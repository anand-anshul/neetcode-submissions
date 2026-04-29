from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1
        n = len(s1)

        count2 = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            count2[s2[r]] += 1

            if r - l + 1 > n:
                if count2[s2[l]] == 1:
                    del count2[s2[l]]
                else:
                    count2[s2[l]] -= 1
                l += 1

            if count1 == count2:
                return True

        return False
