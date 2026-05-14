class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        cd = (arr[-1] - arr[0]) // len(arr)

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != cd:
                return arr[i] + cd
        
        return arr[0]