class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2: return len(arr)
        prev = 0
        left = 0
        max_len = 1

        for right in range(len(arr) - 1):
            if arr[right] > arr[right + 1] and prev != 1:
                prev = 1
            elif arr[right] < arr[right + 1] and prev != -1:
                prev = -1
            else:
                if arr[right] == arr[right + 1]:
                    left = right + 1
                else:
                    left = right
                prev = 1 if arr[right] > arr[right + 1] else -1
            
            max_len = max(max_len, right - left + 2)

        return max_len