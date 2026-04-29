class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)

        for str in strs:
            key = [0] * 26
            for char in str:
                key[ord(char) - ord('a')] += 1
            ana_map[tuple(key)].append(str)

        ana_list = []
        for key, value in ana_map.items():
            ana_list.append(value)
        return ana_list