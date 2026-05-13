class Solution:
    def check(self, nums: List[int]) -> bool:
        new  = nums + nums
        n = len(nums)
        slow = 0
        curLen = 0
        for fast in range(2*n - 1):
            if fast - slow + 1 == n:
                return True
            if new[fast + 1] < new[fast]:
                slow = fast + 1
                continue
        if (2*n - 1) - slow + 1 == n: return True
        return False
            