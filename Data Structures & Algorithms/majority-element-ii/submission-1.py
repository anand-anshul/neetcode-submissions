class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_count = defaultdict(int)
        n = len(nums)
        for num in nums:
            current = num
            num_count[current] += 1
        
        majors = []
        for num, count in num_count.items():
            if count > (n // 3):
                majors.append(num)

        return majors
