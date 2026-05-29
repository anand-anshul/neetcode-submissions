class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            can_reach = i + nums[i]

            if can_reach >= dest:
                dest = i

        return dest == 0
