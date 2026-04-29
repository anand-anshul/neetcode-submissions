class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue


            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return False
            