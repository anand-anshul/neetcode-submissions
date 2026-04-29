class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            stn1 = heapq.heappop(stones)
            stn2 = heapq.heappop(stones)
            if stn1 < stn2:
                heapq.heappush(stones, stn1 - stn2)
        stones.append(0)
        return abs(stones[0])