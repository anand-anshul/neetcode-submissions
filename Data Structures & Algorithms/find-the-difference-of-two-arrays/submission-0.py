class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        ans0 = set()

        for num in nums1:
            if num in set2:
                continue
            ans0.add(num)

        ans1 = set()

        for num in nums2:
            if num in set1:
                continue
            ans1.add(num)

        return [list(ans0), list(ans1)]