class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            prefix[i] = cur
        
        ptr = 0
        for j in range(len(nums) - 1, -1, -1):
            ptr += nums[j]
            postfix[j] = ptr

        for k in range(len(nums)):
            if k - 1 < 0:
                left = 0
            else:
                left = prefix[k - 1]
            if k + 1 > len(nums) - 1:
                right = 0
            else:
                right = postfix[k + 1]    
            
            if left == right:
                return k
        return -1