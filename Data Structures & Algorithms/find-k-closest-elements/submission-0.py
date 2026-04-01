class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        distance = []
        res = []

        for i in arr:
            distance.append(abs(i - x))
        
        count = 0
        while count < k:
            res.append(arr[distance.index(min(distance))])
            distance[distance.index(min(distance))] = 50000000
            count += 1
        
        return sorted(res)
