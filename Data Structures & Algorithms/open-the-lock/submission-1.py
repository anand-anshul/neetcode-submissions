class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(comb):
            res = []
            for i in range(4):
                digit = str((int(comb[i]) + 1) % 10)
                res.append(comb[:i] + digit + comb[i + 1:])
                digit = str((int(comb[i]) - 1 + 10) % 10)
                res.append(comb[:i] + digit + comb[i + 1:])
            return res

        
        visit = set(deadends)
        q = deque()
        q.append("0000")
        turns = 0
        
        while q:
            for i in range(len(q)):
                comb = q.popleft()
                if comb == target:
                    return turns

                for child in children(comb):
                    if child not in visit:
                        q.append(child)
                        visit.add(child)
            turns += 1
        return -1
