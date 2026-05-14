class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pali_expand(left, right, s):
            while (
                left > 0 and right < len(s) - 1 and
                s[left - 1] == s[right + 1]
            ):
                left -= 1
                right += 1
            return left, right - left + 1

        n = len(s)
        start, max_len = 0, 0

        for center in range(n):
            odd_start, odd_len = pali_expand(center, center, s)
            if odd_len > max_len:
                max_len = odd_len
                start = odd_start

            if center < n - 1 and s[center] == s[center + 1]:
                even_start, even_len = pali_expand(center, center + 1, s)
                if even_len > max_len:
                    max_len = even_len
                    start = even_start

        return s[start:start + max_len]