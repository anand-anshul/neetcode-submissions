class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        for num, count in num_count.items():
            heapq.heappush(heap, [-count, num])

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        

        return res