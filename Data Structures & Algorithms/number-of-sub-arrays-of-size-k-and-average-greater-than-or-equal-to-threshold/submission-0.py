class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cursum = 0
        L = 0
        count = 0
        # [2,2,2,2,5,5,5,8]

        for R in range(len(arr)):
            cursum += arr[R]
            if R < k - 1:
                continue
            
            avg = cursum // k
            if avg >= threshold:
                count += 1
            cursum -= arr[L]
            L += 1
        return count
            
