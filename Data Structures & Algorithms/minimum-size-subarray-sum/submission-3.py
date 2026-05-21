class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float('inf')
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                length = right - left + 1
                min_len = min(min_len, length)
                total -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0