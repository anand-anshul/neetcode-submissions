class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist2point = collections.defaultdict(list)
        res = []
        dists = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            dist2point[dist].append(point)
            dists.append(dist)

        heapq.heapify(dists)

        while k > 0:
            length = heapq.heappop(dists)
            res.append(dist2point[length].pop())
            k -= 1
        return res
        
