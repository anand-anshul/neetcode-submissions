class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(len(nums)):
            prefix[i] = nums[i] * pre
            pre = prefix[i]

        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[i] * post
            post = postfix[i]

        output = [1] * len(nums)

        for i in range(len(nums)):
            left = None
            right = None
            if i == 0:
                left = 1
            else:
                left = prefix[i - 1]

            if i == len(nums) - 1:
                right = 1
            else:
                right = postfix[i + 1]

            output[i] = left * right

        return output

        
