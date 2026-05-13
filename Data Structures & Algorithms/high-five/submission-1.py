class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        def average(top_5):
            return sum(top_5) // 5
        
        scores = defaultdict(list)

        for item in items:
            ID, score = item
            scores[ID].append(score)
        
        res = []

        for ID in sorted(scores.keys()):
            score = scores[ID]
            heapq.heapify(score)
            while len(score) > 5:
                heapq.heappop(score)
            top_5_avg = average(score)
            res.append([ID, top_5_avg])

        return res
