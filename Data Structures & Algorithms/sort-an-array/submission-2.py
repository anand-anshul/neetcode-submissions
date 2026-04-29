class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            i = 0
            j = 0
            combined = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    combined.append(left[i])
                    i += 1
                else:
                    combined.append(right[j])
                    j += 1

            if i != len(left):
                combined += left[i:]
            if j != len(right):
                combined += right[j:]

            return combined 

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            length = len(arr)
            left = arr[:length // 2]
            right = arr[length // 2:]

            left_sorted = merge_sort(left)
            right_sorted = merge_sort(right)

            combined_sorted = merge(left_sorted, right_sorted)
            return combined_sorted

        return merge_sort(nums)