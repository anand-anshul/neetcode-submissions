class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def helper(i, cursum, curset):
            if cursum == target:
                subsets.append(curset.copy())
                return
            
            if i >= len(nums) or cursum > target:
                return
            
            curset.append(nums[i])
            helper(i, cursum + nums[i], curset)
            curset.pop()

            helper(i + 1, cursum, curset)

        subsets = []
        helper(0, 0, [])
        return subsets

             
