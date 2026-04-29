class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        sortedLeft = self.sortArray(nums[:n // 2])
        sortedRight = self.sortArray(nums[n // 2:])

        mergedArray = self.mergeArray(sortedLeft, sortedRight)
        return mergedArray

    def mergeArray(self, left, right):
        array = []
        i, l, r = 0, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array.append(left[l])
                l += 1
            else:
                array.append(right[r])
                r += 1
            i += 1

        if l < len(left):
            array += left[l:]
        if r < len(right):
            array += right[r:]
        
        return array




    