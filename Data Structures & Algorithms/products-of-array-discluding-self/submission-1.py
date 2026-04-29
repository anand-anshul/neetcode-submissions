class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [1] * len(nums)

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(len(nums)):
            prefix[i] = pre * nums[i]
            pre = prefix[i]
        
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = post * nums[j]
            post = postfix[j]

        for k in range(len(nums)):
            if k == 0:
                res[k] = postfix[k + 1]
            elif k == len(nums) - 1:
                res[k] = prefix[k - 1]
            else:
                res[k] = prefix[k - 1] * postfix[k + 1]

        return res