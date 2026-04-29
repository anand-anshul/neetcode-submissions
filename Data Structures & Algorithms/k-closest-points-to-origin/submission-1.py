class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # (dist, [x, y])

        res = []

        heap = []

        for point in points:
            x, y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, [x, y]))

        for i in range(k):
            point = heapq.heappop(heap)
            res.append(point[1])

        return res
