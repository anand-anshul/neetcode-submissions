class Solution:
    def maxDifference(self, s: str) -> int:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        max_odd = 0
        min_even = float('inf')
        for c, f in counts.items():
            if f % 2 == 0:
                min_even = min(min_even, f)
            else:
                max_odd = max(max_odd, f)

        return max_odd - int(min_even)