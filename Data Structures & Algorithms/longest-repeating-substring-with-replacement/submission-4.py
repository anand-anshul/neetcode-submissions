class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_count = defaultdict(int)
        max_length = 0
        max_count = 0

        for right in range(len(s)):
            l_char = s[left]
            r_char = s[right]
            
            char_count[r_char] += 1
            max_count = max(max_count, char_count[r_char])

            while right - left + 1  - max_count > k:
                char_count[l_char] -= 1
                left += 1
            window_size = right - left + 1 
            max_length = max(max_length, window_size)
        return max_length

            

