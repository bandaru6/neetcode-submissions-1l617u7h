class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = []
        res = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, [-n, i])


            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            
            if len(heap) >= k:
                res.append(-heap[0][0])

        return res






