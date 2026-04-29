class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, curCap = 1, cap
            for w in weights:
                if curCap < w:
                    ships += 1
                    if ships > days:
                        return False
                    curCap = cap
                curCap -= w
            return True
                
                
                
        
        
        

        while l <= r:
            c = (l + r) // 2
            

            if canShip(c):
                res = min(res, c)
                r = c - 1
            else:
                l = c + 1

        return res
            
