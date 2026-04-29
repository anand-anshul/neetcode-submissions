class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key2ana = defaultdict(list)

        for str in strs:
            key = [0] * 26
            for char in str:
                key[ord(char) - ord('a')] += 1
            key2ana[tuple(key)].append(str)
        
        res = []
        for key, ana_list in key2ana.items():
            res.append(ana_list)

        return res