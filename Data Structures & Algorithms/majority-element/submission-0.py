class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        res = maxcount = 0

        for num in nums:
            freq[num] += 1
            if maxcount < freq[num]:
                res = num
                maxcount = freq[num]
        return res