class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for ele, freq in count.items():
            if freq > (n // 2):
                return ele
        return 0
        
