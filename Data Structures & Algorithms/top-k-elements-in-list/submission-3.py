class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = defaultdict(int)

        for num in nums:
            num2freq[num] += 1

        heap = []

        for num, count in num2freq.items():
            heapq.heappush(heap, (-count, num))

        res = []

        for i in range(k):
            neg_count, num = heapq.heappop(heap)
            res.append(num)

        return res