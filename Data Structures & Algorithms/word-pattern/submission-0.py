class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        char2word = {}
        word2char = {}

        for c, w in zip(pattern, words):
            if c in char2word and char2word[c] != w:
                return False
            if w in word2char and word2char[w] != c:
                return False

            char2word[c] = w
            word2char[w] = c

        return True