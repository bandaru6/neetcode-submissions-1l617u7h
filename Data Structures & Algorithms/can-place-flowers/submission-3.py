class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        res = 0
        for x in range(len(flowerbed)):
            if x == 0 and flowerbed[x] == 0:
                if flowerbed[x+1] == 0:
                    flowerbed[x] == 1
                    res += 1
            if x == len(flowerbed) - 1 and flowerbed[len(flowerbed)-1] == 0:
                if flowerbed[x-1] == 0:
                    flowerbed[x] == 1
                    res += 1
            if flowerbed[x] == 0:
                if x + 1 < len(flowerbed) and x - 1 >= 0:
                    if flowerbed[x+1] == 0 and flowerbed[x-1] == 0:
                        res += 1
                        flowerbed[x] = 1
            if res >= n:
                return True
        return False 