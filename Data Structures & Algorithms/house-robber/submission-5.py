class Solution:
    def rob(self, nums: List[int]) -> int:
        def top_down(i, arr, memo):
            if i == 0:
                return arr[0]
            if i == 1:
                return max(arr[0], arr[i])
            if i in memo:
                return memo[i]

            memo[i] = max(top_down(i - 1, arr, memo), arr[i] + top_down(i - 2, arr, memo))
            return memo[i]

        largest = top_down(len(nums) - 1, nums, {})
        return largest