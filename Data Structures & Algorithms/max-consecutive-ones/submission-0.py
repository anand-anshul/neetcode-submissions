class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 0:
                max_count = max(max_count, count)
                count = 0
                continue
            count += num

        return max(max_count, count)

            