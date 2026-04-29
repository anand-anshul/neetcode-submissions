# Given an array nums 
# of size n, 
# return the majority element.

# The majority element is the element that 
# appears more than ⌊n / 2⌋ times in the array. 

# You may assume that 
# the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        
        for num in nums:
            num_count[num] += 1
        
        max_num = nums[0]
        for num, count in num_count.items():
            if count > num_count[max_num]:
                max_num = num
        
        return max_num
    







