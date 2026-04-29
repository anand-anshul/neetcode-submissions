class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R, res, prev = 0, 1, 1, ""
        # [2,< 4, > 3,> 2 r,5,1,4]

        while R < len(arr):
            if arr[R - 1] > arr[R] and prev != '>':
                res = max(R - L + 1, res)
                R += 1
                prev = '>'

            elif arr[R - 1] < arr[R] and prev != '<':
                res = max(R - L + 1, res)
                R += 1
                prev = '<'
            else:
                if arr[R - 1] == arr[R]:
                    R += 1
                L = R - 1
                prev = ''
        return res
