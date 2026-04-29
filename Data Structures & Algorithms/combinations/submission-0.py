class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(i, curcomb, combs, n, k):
            if len(curcomb) == k:
                combs.append(curcomb.copy())
                return
            
            if i > n:
                return

            curcomb.append(i)
            helper(i + 1, curcomb, combs, n, k)
            curcomb.pop()

            helper(i + 1, curcomb, combs, n, k)

        combs = []
        helper(1, [], combs, n, k)
        return combs
