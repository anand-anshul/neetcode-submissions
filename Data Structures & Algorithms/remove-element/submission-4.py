class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        drop_ptr = 0

        for pick_ptr in range(len(nums)):
            if nums[pick_ptr] == val:
                continue
            nums[drop_ptr] = nums[pick_ptr]
            drop_ptr += 1
        return drop_ptr