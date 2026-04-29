class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def dfs(i, init):
            if i >= len(nums):
                if init == target:
                    return 1
                else:
                    return 0
            if (i, init) in memo:
                return memo[(i, init)]
            
            memo[(i, init)] = dfs(i + 1, init + nums[i]) + dfs(i + 1, init - nums[i])

            return memo[(i,init)]

        
        return dfs(0, 0)
            