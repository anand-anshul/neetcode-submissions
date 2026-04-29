class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_1 = 0
        ptr_2 = 0

        merged = ""

        while ptr_1 < len(word1) and ptr_2 < len(word2):
            merged += word1[ptr_1]
            merged += word2[ptr_2]
            ptr_1 += 1
            ptr_2 += 1

        if ptr_1 != len(word1):
            merged += word1[ptr_1:]
        if ptr_2 != len(word2):
            merged += word2[ptr_2:]

        return merged