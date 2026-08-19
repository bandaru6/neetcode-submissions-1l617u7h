class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2

            time = 0 
            for pile in piles:
                time += math.ceil(pile / mid)
            
            print("time:", time)
            print("mid:", mid)

            if time <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l

