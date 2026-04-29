class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []
        for n, f in count.items():
            heapq.heappush(heap, (-f, n))

        res = []
        for i in range(k):
            tup = heapq.heappop(heap)
            res.append(tup[1])
        return res