class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for src, dst, time in times:
            graph[src].append((dst, time))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, t1)
            neis = graph[n1]
            for n2, t2 in neis:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t2 + t1, n2))

        return t if len(visit) == n else -1
