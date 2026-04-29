class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        
        while len(heap) > 1:
            first, second = -1 * heapq.heappop(heap), -1 * heapq.heappop(heap)
            if abs(first - second) > 0:
                heapq.heappush(heap, -1 * abs(first - second))
        heap.append(0)
        return -1 * heap[0]