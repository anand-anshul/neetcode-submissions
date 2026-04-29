class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i, j = 0, 0
        res = []

        while i < len(w1) and j < len(w2):
            res.append(w1[i])
            res.append(w2[j])
            i += 1
            j += 1

        while i < len(w1):
            res.append(w1[i])
            i += 1
        while j < len(w2):
            res.append(w2[j])
            j += 1

        return "".join(res)
        
        
