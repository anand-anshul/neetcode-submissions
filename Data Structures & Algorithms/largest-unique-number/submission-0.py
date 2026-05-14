class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = Counter(nums)

        max_num = -1
        for num, freq in freq_map.items():
            if freq == 1:
                max_num = max(max_num, num)
        return max_num