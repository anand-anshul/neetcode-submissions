class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        minDist = len(wordsDict)

        for i in range(minDist):
            if wordsDict[i] == word1:
                i1 = i
            if wordsDict[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                minDist = min(minDist, abs(i1 - i2))

        return minDist