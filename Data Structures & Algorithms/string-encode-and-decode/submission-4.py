class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded


        # 3#abc2#it


    def decode(self, s: str) -> List[str]:
        decoded = []
        j = 0
        i = 0
        while i < len(s):
            if s[i] == '#':
                str_len = int(s[j:i])
                unit = s[i + 1 : i + str_len + 1]
                decoded.append(unit)
                i += str_len + 1
                j = i
            else:
                i += 1 
        return decoded