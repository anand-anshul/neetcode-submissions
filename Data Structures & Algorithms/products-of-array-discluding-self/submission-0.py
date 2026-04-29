class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [1] * len(nums)

        lcur = 1
        for i in range(len(nums)):
            lcur *= nums[i]
            prefix[i] = lcur
        
        rcur = 1
        for j in range(len(nums) - 1, -1, -1):
            rcur *= nums[j]
            postfix[j] = rcur

        for k in range(len(nums)):
            if k - 1 < 0:
                left = 1
            else:
                left = prefix[k - 1]
            
            if k + 1 > len(nums) - 1:
                right = 1
            else:
                right = postfix[k + 1]

            res[k] = left * right

        return res   


         