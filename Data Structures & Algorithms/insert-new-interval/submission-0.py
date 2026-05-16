class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for B in intervals[1:]:
            A = merged[-1]
            if A[1] < B[0]:
                merged.append(B)
            else:
                interval = [A[0], max(A[1], B[1])]
                merged[-1] = interval

        return merged