class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for b in bills:
            if b == 20:
                if change[5] >= 3:
                    change[5] -= 3
                elif change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    return False
            elif b == 10:
                if change[5] >= 1:
                    change[5] -= 1
                else:
                    return False
            change[b] += 1

        return True