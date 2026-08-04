class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        hi = max(piles)
        res = hi
        while l < hi:
            m = (l + hi) // 2
            #print(l, hi, m)
            c = 0
            for pile in piles: 
                c += math.ceil(pile / m)
            #print(c)
            if c > h:
                l = m + 1
            elif c <= h:
                hi = m
                res = min(res, m)

        
        return res
                
                 