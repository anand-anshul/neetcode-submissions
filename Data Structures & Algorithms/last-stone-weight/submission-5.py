class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            res = abs(first - second)
            if res != 0:
                heapq.heappush(heap, -res)

        return -heapq.heappop(heap) if heap else 0        

