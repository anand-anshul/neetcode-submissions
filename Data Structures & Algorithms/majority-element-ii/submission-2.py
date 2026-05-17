class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        m = n // 3
        res = []
        for num, count in count.items():
            if count > m:
                res.append(num)

        return res
