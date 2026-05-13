class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums.copy()

        heap = [(val, i) for i, val in enumerate(nums)]

        heapq.heapify(heap)

        for _ in range(k):
            val, i = heapq.heappop(heap)
            res[i] *= multiplier
            heapq.heappush(heap, (res[i], i))

        return res
        
