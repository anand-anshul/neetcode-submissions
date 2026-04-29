class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref_str = strs[0]
        lcp = ""

        for c_i in range(len(ref_str)):
            ref_char = ref_str[c_i]
            for str in strs:
                if c_i == len(str) or str[c_i] != ref_char:
                    return lcp
            lcp += ref_char
        return lcp