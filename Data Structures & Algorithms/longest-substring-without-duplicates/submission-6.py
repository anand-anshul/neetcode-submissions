class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        longest = 0

        for right in range(len(s)):
            c = s[right]
            while c in window:
                window.remove(s[left])
                left += 1
            length = right - left + 1
            window.add(c)
            longest = max(longest, length)
        return longest