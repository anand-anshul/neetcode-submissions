class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j < len(s):
                j += 1
                i += 1
            else:
                break

        return i