class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x < y:
                heapq.heappush(maxHeap, x - y)
                
        maxHeap.append(0)
        return abs(maxHeap[0]) 

