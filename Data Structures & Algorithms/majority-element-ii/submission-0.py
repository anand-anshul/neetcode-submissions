class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        n = len(nums)

        res = []
        for num, freq in count.items():
            if freq > n // 3:
                res.append(num)
        
        return res