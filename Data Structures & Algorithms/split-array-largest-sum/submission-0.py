class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            cursum = 0

            for n in nums:
                cursum += n
                if cursum > largest:
                    subarray += 1
                    cursum = n
            return subarray <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
