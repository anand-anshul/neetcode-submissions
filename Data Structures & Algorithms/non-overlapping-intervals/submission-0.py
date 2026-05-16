class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = 0
        A = intervals[0]

        for B in intervals[1:]:
            if A[1] <= B[0]:
                A = B
            else:
                res += 1
                A = [A[0], min(A[1], B[1])]

        return res 