class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, [-value, key])

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res