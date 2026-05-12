class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(str1, str2):
            mp = {}
            for i in range(len(str1)):
                if str1[i] in mp and mp[str1[i]] != str2[i]:
                    return False
                mp[str1[i]] = str2[i]
            return True

        if len(s) != len(t):
            return False

        return helper(s, t) and helper(t, s)