class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for B in intervals[1:]:
            A = merged[-1]

            if A[1] < B[0]:
                merged.append(B)
            else:
                new_interval = [A[0], max(A[1], B[1])]
                merged[-1] = new_interval

        return merged