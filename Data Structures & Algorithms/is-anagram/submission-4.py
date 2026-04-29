class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            s_map[s_char] += 1
            t_map[t_char] += 1

        return s_map == t_map