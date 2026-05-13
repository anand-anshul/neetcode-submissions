class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []

        for num in nums:
            sq = num * num
            heapq.heappush(heap, sq)

        res = []

        while heap:
            top = heapq.heappop(heap)
            res.append(top)

        return res