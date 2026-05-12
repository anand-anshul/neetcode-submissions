class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        word = ""
        for c in s:
            
            if c == " ":
                if word:
                    words.append(word)
                word = ""
            else:
                word += c
        if word:
            words.append(word)

        return len(words[-1])