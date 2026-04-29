class Solution:
    def jump(self, nums: List[int]) -> int:
        res = []
        
        def dfs(i, cur):
            if i >= len(nums) - 1:
                res.append(cur)
                return
            
            end = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                cur += 1
                dfs(j, cur)
                cur -= 1

        dfs(0, 0)
        return min(res)

