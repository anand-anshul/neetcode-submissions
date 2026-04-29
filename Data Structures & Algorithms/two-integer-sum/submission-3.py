class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen2idx = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen2idx:
                return [seen2idx[complement], i]
            seen2idx[nums[i]] = i
        
            
