class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = 0
        seen = defaultdict(int)
        maxf = 0
        for R in range(len(s)):
            seen[s[R]] += 1
            maxf = max(maxf, seen[s[R]])
            while (R - L + 1) - maxf > k:
                seen[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length
