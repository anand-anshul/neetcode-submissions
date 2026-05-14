class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #rob(i) = max(house[i] + rob(i - 2), rob(i - 1))
        def robbery(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            if len(arr) == 2:
                return max(arr[0], arr[1]) 
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
            return dp[len(arr) - 1]

        rob1 = robbery(nums[:len(nums) - 1])
        rob2 = robbery(nums[1:])

        return max(rob1, rob2)