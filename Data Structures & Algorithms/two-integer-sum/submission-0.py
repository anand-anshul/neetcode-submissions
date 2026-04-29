class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in prevMap:
                return [prevMap[comp], i]
            prevMap[n] = i
        return